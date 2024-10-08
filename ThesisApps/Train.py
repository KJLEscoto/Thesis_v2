import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import filedialog
import cv2
import mediapipe as mp
import numpy as np
import csv
import threading
import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import logging

# Configure logging
logging.basicConfig(
    filename='motion_feed_app.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Set appearance mode and theme
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('blue')

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

def file_exists(file_path):
    return os.path.isfile(file_path)

class MotionFeedApp:

    def __init__(self, root):
        self.root = root
        self.file_name_var = tk.StringVar()
        self.training_handler = TrainingHandler(self.root)
        self.setup_ui()

    def setup_ui(self):
        self.root.title('Motion Feed GUI')
        self.root.geometry('400x400')
        ctk.CTkLabel(self.root, text='Motion Feed', font=('Helvetica', 20)).pack(pady=10)
        ctk.CTkLabel(self.root, text='Choose an option to add a motion:').pack(pady=10)
        ctk.CTkButton(self.root, text='Via Live', command=self.show_webcam_gui).pack(pady=10)
        ctk.CTkButton(self.root, text='Via Folder', command=self.show_folder_gui).pack(pady=10)

    def upload_file(self):
        file = filedialog.askopenfile()
        if file:
            self.file_name_var.set(file.name)

    def enable_start_training_button(self):
        if hasattr(self, 'start_training_button'):
            self.start_training_button.configure(state='normal')
            logging.info('Start Training button enabled.')
        else:
            logging.error('Start Training button not found.')

    def show_webcam_gui(self):
        self.root.withdraw()
        webcam_window = ctk.CTkToplevel(self.root)
        webcam_window.title('Webcam Processing')
        webcam_window.geometry('400x250')
        ctk.CTkLabel(webcam_window, text='Class Name:').pack(pady=5)
        file_name_entry = ctk.CTkEntry(webcam_window, textvariable=self.file_name_var)
        file_name_entry.pack()
        ctk.CTkButton(webcam_window, text='Start Webcam', command=self.start_webcam).pack(pady=20)
        csv_file = 'coords.csv'
        self.start_training_button = ctk.CTkButton(
            webcam_window,
            text='Start Training',
            state='disabled',
            command=lambda: self.training_handler.start_training(csv_file)
        )
        self.start_training_button.pack(pady=10)
        webcam_window.focus_set()
        webcam_window.wait_window()
        self.root.deiconify()

    def start_webcam(self):
        class_name = self.file_name_var.get()
        csv_file = 'coords.csv'
        if class_name:
            self.root.withdraw()
            threading.Thread(target=self.main, args=(class_name, csv_file), daemon=True).start()
        else:
            msgbox.showinfo(title='Alert', message='Please enter a class name before starting')
            logging.warning('User attempted to start webcam without entering a class name.')

    def main(self, class_name, csv_file):
        cap = cv2.VideoCapture(0)
        self.setup_window('Processing Webcam Feed')
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    msgbox.showinfo(title='Alert', message='Error: Could not read from webcam')
                    logging.error('Could not read from webcam.')
                    break
                frame = self.process_frame(frame)
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = holistic.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                self.draw_landmarks(image, results)
                self.export_landmarks_to_csv(results, class_name, csv_file)
                cv2.imshow('Processing Webcam Feed', image)
                if cv2.waitKey(10) & 255 == ord('q') or cv2.getWindowProperty('Processing Webcam Feed', cv2.WND_PROP_VISIBLE) < 1:
                    self.start_training_button.configure(state='normal')
                    logging.info('Webcam processing interrupted by user.')
                    break
        cap.release()
        cv2.destroyAllWindows()
        msgbox.showinfo(title='Processing Finished', message='Processing finished. You can now train the new data.')
        logging.info('Webcam processing finished.')
        self.root.after(0, self.enable_start_training_button)

    def setup_window(self, window_name, width=1280, height=720):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
        cv2.resizeWindow(window_name, width, height)

    def process_frame(self, frame, target_width=1280):
        height, width = frame.shape[:2]
        aspect_ratio = width / height
        new_height = int(target_width / aspect_ratio)
        return cv2.resize(frame, (target_width, new_height))

    def draw_landmarks(self, image, results):
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
            )
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2)
            )
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
            )

    def export_landmarks_to_csv(self, results, class_name, csv_file):
        if results.pose_landmarks:
            pose = results.pose_landmarks.landmark
            pose_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())
            pose_row.insert(0, class_name)
            try:
                # Check if file exists to write header only once
                header = False
                if not file_exists(csv_file):
                    header = ['class'] + [f'landmark_{i}_{coord}' for i in range(33) for coord in ['x', 'y', 'z', 'visibility']]
                with open(csv_file, mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    if header:
                        csv_writer.writerow(header)
                        logging.info('CSV header written.')
                    csv_writer.writerow(pose_row)
                    f.flush()
            except Exception as e:
                msgbox.showinfo(title='Alert', message=f'Error exporting data: {e}')
                logging.error(f'Error exporting data: {e}')

    def show_folder_gui(self):
        self.root.withdraw()
        folder_window = ctk.CTkToplevel(self.root)
        folder_window.title('Folder Selection')
        folder_window.geometry('400x400')  # Adjusted height for progress bar

        ctk.CTkLabel(folder_window, text='Select Video Directory:').pack(pady=5)
        folder_path_var = tk.StringVar()
        folder_entry = ctk.CTkEntry(folder_window, textvariable=folder_path_var, state='disabled', width=300)
        folder_entry.pack(pady=5)
        ctk.CTkButton(folder_window, text='Browse', command=lambda: self.browse_folder(folder_path_var)).pack(pady=5)

        ctk.CTkLabel(folder_window, text='Class Name:').pack(pady=5)
        class_name_var = tk.StringVar()
        class_name_entry = ctk.CTkEntry(folder_window, textvariable=class_name_var, width=300)
        class_name_entry.pack(pady=5)

        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ctk.CTkProgressBar(folder_window, variable=self.progress_var, width=300)
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)

        ctk.CTkButton(
            folder_window,
            text='Start Processing',
            command=lambda: self.start_video_processing(folder_path_var.get(), class_name_var.get())
        ).pack(pady=10)

        self.start_training_button = ctk.CTkButton(
            folder_window,
            text='Start Training',
            state='disabled',
            command=lambda: self.training_handler.start_training('coords.csv')
        )
        self.start_training_button.pack(pady=10)

        folder_window.focus_set()
        folder_window.wait_window()
        self.root.deiconify()

    def browse_folder(self, folder_path_var):
        folder_path = filedialog.askdirectory()
        if folder_path:
            folder_path_var.set(folder_path)

    def start_video_processing(self, video_dir, class_name):
        csv_file = 'coords.csv'
        if video_dir and class_name:
            processor = VideoPoseProcessor(video_dir, class_name, csv_file, self)
            threading.Thread(target=processor.process_videos, daemon=True).start()
            logging.info(f'Started processing videos in directory: {video_dir} with class name: {class_name}')
        else:
            msgbox.showinfo(title='Alert', message='Please provide both a video directory and a class name.')
            logging.warning('User attempted to start video processing without providing both video directory and class name.')

    def close_folder_gui(self, folder_window):
        folder_window.destroy()
        self.root.deiconify()

class TrainingHandler:

    def __init__(self, root):
        self.root = root
        self.fit_models = {}
        self.results_window = None

    def start_training(self, csv_file):
        try:
            df = pd.read_csv(csv_file)
            if 'class' in df.columns:
                X = df.drop('class', axis=1)
                y = df['class']
            else:
                y = df.iloc[:, 0]
                X = df.iloc[:, 1:]
            # Data validation
            if X.empty or y.empty:
                msgbox.showinfo(title='Error', message='Training data is empty or improperly formatted.')
                logging.error('Training data is empty or improperly formatted.')
                return
            if X.isnull().values.any() or y.isnull().values.any():
                msgbox.showinfo(title='Error', message='Training data contains missing values.')
                logging.error('Training data contains missing values.')
                return
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)
            pipelines = {
                'lr': make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
                'rc': make_pipeline(StandardScaler(), RidgeClassifier()),
                'rf': make_pipeline(StandardScaler(), RandomForestClassifier()),
                'gb': make_pipeline(StandardScaler(), GradientBoostingClassifier())
            }
            results = {}
            for algo, pipeline in pipelines.items():
                model = pipeline.fit(X_train, y_train)
                self.fit_models[algo] = model
                yhat = model.predict(X_test)
                score = accuracy_score(y_test, yhat)
                results[algo] = score
                logging.info(f'Trained {algo} with accuracy: {score:.2f}')
            self.show_results(results)
        except Exception as e:
            msgbox.showinfo(title='Training Error', message=f'An error occurred during training: {e}')
            logging.error(f'An error occurred during training: {e}')

    def show_results(self, results):
        self.root.withdraw()
        self.results_window = ctk.CTkToplevel()
        self.results_window.title('Training Results')
        self.results_window.geometry('300x300')

        # Scrollable Frame for Results
        scrollable_frame = ctk.CTkScrollableFrame(self.results_window, width=280, height=250)
        scrollable_frame.pack(pady=10, padx=10, fill='both', expand=True)

        for algo, score in results.items():
            result_text = f'{algo}: {score:.2f}'
            ctk.CTkLabel(scrollable_frame, text=result_text, anchor='w').pack(pady=2, fill='x')
            select_button = ctk.CTkButton(
                scrollable_frame,
                text='Select Algo',
                command=lambda a=algo: self.select_algorithm(a)
            )
            select_button.pack(pady=2, fill='x')

    def select_algorithm(self, algo):
        model = self.fit_models.get(algo)
        if model:
            file_path = filedialog.asksaveasfilename(
                defaultextension='.pkl',
                filetypes=[('Pickle files', '*.pkl'), ('All files', '*.*')],
                title=f'Save {algo} Model'
            )
            if file_path:
                try:
                    with open(file_path, 'wb') as f:
                        pickle.dump(model, f)
                    logging.info(f'{algo} model saved as {file_path}')
                    msgbox.showinfo(title='Success', message=f'{algo} model saved as {file_path}')
                    self.results_window.destroy()
                except Exception as e:
                    msgbox.showinfo(title='Error', message=f'Failed to save model: {e}')
                    logging.error(f'Failed to save model: {e}')

class VideoPoseProcessor:

    def __init__(self, video_dir, class_name, csv_file, app):
        self.video_dir = video_dir
        self.class_name = class_name
        self.csv_file = csv_file
        self.app = app

    def process_videos(self):
        try:
            video_files = [f for f in os.listdir(self.video_dir) if f.endswith('.mp4') or f.endswith('.avi')]
            total_videos = len(video_files)
            if total_videos == 0:
                msgbox.showinfo(title='No Videos', message='No video files found in the selected directory.')
                logging.warning('No video files found in the selected directory.')
                return
            for idx, filename in enumerate(video_files, start=1):
                video_path = os.path.join(self.video_dir, filename)
                self.process_video(video_path)
                # Update progress
                progress = idx / total_videos * 100
                self.app.progress_var.set(progress)
                self.app.progress_bar.set(progress / 100)  # Assuming progress_bar ranges from 0 to 1
                self.app.progress_bar.update()
                logging.info(f'Processed video {idx}/{total_videos}: {filename}')
        except Exception as e:
            msgbox.showinfo(title='Processing Error', message=f'An error occurred during video processing: {e}')
            logging.error(f'An error occurred during video processing: {e}')
        finally:
            logging.info('Video processing finished. Enabling Start Training button.')
            msgbox.showinfo(title='Processing Finished', message='Processing finished. You can now train the new data.')
            self.app.root.after(0, self.app.enable_start_training_button)

    def process_video(self, video_path):
        try:
            logging.info(f'Starting processing of video: {video_path}')
            cap = cv2.VideoCapture(video_path)
            with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    frame = self.process_frame(frame)
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
                    results = holistic.process(image)
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    self.draw_landmarks(image, results)
                    self.export_landmarks_to_csv(results, self.class_name)
                    cv2.imshow('Processing Video', image)
                    if cv2.waitKey(10) & 255 == ord('q') or cv2.getWindowProperty('Processing Video', cv2.WND_PROP_VISIBLE) < 1:
                        break
            cap.release()
            cv2.destroyAllWindows()
            logging.info(f'Finished processing of video: {video_path}')
        except Exception as e:
            msgbox.showinfo(title='Video Processing Error', message=f'An error occurred while processing {video_path}: {e}')
            logging.error(f'An error occurred while processing {video_path}: {e}')

    def process_frame(self, frame, target_width=1280):
        height, width = frame.shape[:2]
        aspect_ratio = width / height
        new_height = int(target_width / aspect_ratio)
        return cv2.resize(frame, (target_width, new_height))

    def draw_landmarks(self, image, results):
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(80, 22, 10), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(80, 44, 121), thickness=2, circle_radius=2)
            )
        if results.left_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(121, 44, 250), thickness=2, circle_radius=2)
            )
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
            )

    def export_landmarks_to_csv(self, results, class_name):
        if results.pose_landmarks:
            pose = results.pose_landmarks.landmark
            pose_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())
            pose_row.insert(0, class_name)
            try:
                # Check if file exists to write header only once
                header = False
                if not file_exists(self.csv_file):
                    header = ['class'] + [f'landmark_{i}_{coord}' for i in range(33) for coord in ['x', 'y', 'z', 'visibility']]
                with open(self.csv_file, mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    if header:
                        csv_writer.writerow(header)
                        logging.info('CSV header written.')
                    csv_writer.writerow(pose_row)
                    f.flush()
            except Exception as e:
                msgbox.showinfo(title='Alert', message=f'Error exporting data: {e}')
                logging.error(f'Error exporting data: {e}')

if __name__ == '__main__':
    root = ctk.CTk()
    app = MotionFeedApp(root)
    root.mainloop()
