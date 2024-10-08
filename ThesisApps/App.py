import customtkinter as ctk
from customtkinter import E, INSERT, LEFT, N, NE, NS, ON, S, SE, W, X, Y
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
from flask import Flask, Response
import cv2
import mediapipe as mp
import numpy as np
import pickle
import pandas as pd
import os
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')
import mysql.connector
snapshot_dir = ''
model_path = ''
model = None
app = Flask(__name__)
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mydb = mysql.connector.connect(host='localhost', user='root', password='', database='thesis_bscs2024')
previous_classes = []
action_counts = {'looking_around': 0, 'looking_down': 0, 'holding_pocket': 0}
message_displayed = False
message_display_duration = 30
message_frame_count = 0
start_time_looking_down = None
duration_threshold = timedelta(seconds=3)

def generate_frames():
    global previous_classes, action_counts, message_displayed, message_frame_count, start_time_looking_down

    # data input
    cap = cv2.VideoCapture(0)  # Adjust camera index as needed
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    

    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Recolor Feed
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False        

            # Make Detections
            results = holistic.process(image)

            # Recolor image back to BGR for rendering
            image.flags.writeable = True   
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            try:
                pose = results.pose_landmarks.landmark 
                pose_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())
                
                # make detections
                X = pd.DataFrame([pose_row])
                body_language_class = model.predict(X)[0]
                body_language_prob = model.predict_proba(X)[0]

                # coords for display
                coords = tuple(np.multiply(
                    np.array(
                        (results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EAR].x, 
                         results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EAR].y)),
                    [640, 480]).astype(int))

                # font and display control
                cv2.rectangle(image, (coords[0], coords[1]+5), 
                              (coords[0]+len(body_language_class)*20, coords[1]-30), 
                              (245, 117, 16), -1)
                cv2.putText(image, body_language_class, coords, 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                # status box
                center_x = frame_width // 2
                cv2.rectangle(image, (center_x - 125, 100), (center_x + 125, 60), (245, 117, 16), -1)

                # actual status box
                cv2.putText(image, 'CLASS', (center_x - 30, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, body_language_class.split(' ')[0], (center_x - 35, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(image, 'PROB', (center_x - 110, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(round(body_language_prob[np.argmax(body_language_prob)], 2)), (center_x - 115, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                # Track actions for potential theft detection
                previous_classes.append(body_language_class)
                if len(previous_classes) > 10:
                    previous_classes.pop(0)

                # Looking around logic
                if len(set(previous_classes[-3:])) > 1 and all(c in ['left', 'right', 'down'] for c in previous_classes[-3:]):
                    action_counts['looking_around'] += 1
                    previous_classes = []  # Reset to track next sequence

                # Holding pocket logic
                if body_language_class == 'pocket':
                    action_counts['holding_pocket'] += 1

                # Looking down logic
                if body_language_class == 'down':
                    if start_time_looking_down is None:
                        start_time_looking_down = datetime.now()
                    elif datetime.now() - start_time_looking_down >= duration_threshold:
                        action_counts['looking_down'] += 1
                        start_time_looking_down = None  # Reset after counting
                else:
                    start_time_looking_down = None

                # Check for potential theft conditions
                if sum(value >= 1 for value in action_counts.values()) >= 2:
                    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    # Save snapshot to the specified directory with timestamped filename
                    file_name = f"snapshot_{current_time}.jpg"
                    file_path = os.path.join(snapshot_dir, file_name)
                    print(f"Saving snapshot at {file_path}")
                    success = cv2.imwrite(file_path, image)
                    if success:
                        print(f"Snapshot saved successfully at {file_path}")
                    else:
                        print(f"Failed to save snapshot at {file_path}")

                    # Insert data into MySQL database
                    try:
                        cursor = mydb.cursor()
                        sql = "INSERT INTO trains (motion_name, threshold, level, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
                        threshold_value = float(round(body_language_prob[np.argmax(body_language_prob)], 2))
                        val = (current_time, threshold_value, "potential_theft", current_time, current_time)
                        cursor.execute(sql, val)
                        mydb.commit()
                        print("Data inserted into MySQL database")
                    except Exception as e:
                        print("Error inserting data into MySQL database:", e)
                    finally:
                        cursor.close()

                    message_displayed = True 
                    message_frame_count = 0
                    action_counts = {'looking_around': 0, 'looking_down': 0, 'holding_pocket': 0}  # Reset counters

            except Exception as e:
                print(e)
                pass

            # Display the frame and message if needed
            if message_displayed:
                cv2.putText(image, "Potential Theft Detected!", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
                message_frame_count += 1
                if message_frame_count > message_display_duration:
                    message_displayed = False

            # Display the action counts in the center of the screen
            action_text = f"Looking around: {action_counts['looking_around']} | Looking down: {action_counts['looking_down']} | Holding pocket: {action_counts['holding_pocket']}"
            text_size = cv2.getTextSize(action_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            text_x = (frame_width - text_size[0]) // 2
            text_y = (frame_height - text_size[1]) // 2
            cv2.putText(image, action_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def start_flask_app():
    app.run(debug=False, use_reloader=False)

def select_snapshot_directory():
    global snapshot_dir
    snapshot_dir = filedialog.askdirectory(title='Select Snapshot Directory')
    if snapshot_dir:
        snapshot_label.configure(text=f'Snapshot Directory: {snapshot_dir}')
    else:
        messagebox.showerror('Error', 'No directory selected!')

def select_model_file():
    global model_path, model
    model_path = filedialog.askopenfilename(title='Select Model File', filetypes=[('Pickle files', '*.pkl')])
    if model_path:
        model_label.configure(text=f'Model File: {model_path}')
        try:
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            messagebox.showinfo('Success', 'Model loaded successfully!')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to load model: {e}')
    else:
        messagebox.showerror('Error', 'No model file selected!')

def create_gui():
    root = ctk.CTk()
    root.title('Snapshot and Model Selector')
    root.geometry('400x250')
    select_snapshot_button = ctk.CTkButton(root, text='Select Snapshot Directory', command=select_snapshot_directory)
    select_snapshot_button.pack(pady=10)
    global snapshot_label
    snapshot_label = ctk.CTkLabel(root, text='Snapshot Directory: Not selected')
    snapshot_label.pack()
    select_model_button = ctk.CTkButton(root, text='Select Model File', command=select_model_file)
    select_model_button.pack(pady=10)
    global model_label
    model_label = ctk.CTkLabel(root, text='Model File: Not selected')
    model_label.pack()

    def on_start_button_click():
        if not snapshot_dir:
            messagebox.showerror('Error', 'Snapshot directory is not selected!')
            return
        if not model_path:
            messagebox.showerror('Error', 'Model file is not selected!')
            return
        Thread(target=start_flask_app).start()
        messagebox.showinfo('Success', 'Flask API Started!')

    def handle_start_and_hide():
        on_start_button_click()
        if snapshot_dir and model_path:
            root.withdraw()
    start_button = ctk.CTkButton(root, text='Start', command=handle_start_and_hide)
    start_button.pack(pady=20)
    root.mainloop()
if __name__ == '__main__':
    create_gui()