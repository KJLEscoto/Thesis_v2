let alertSound;

// Ensure Audio is only initialized on the client-side
if (typeof window !== 'undefined') {
    alertSound = new Audio('/alert_2.mp3');
}

// Export function to stop and reset the alert sound
export const alertStop = () => {
if (alertSound) {
    alertSound.pause();
    alertSound.currentTime = 0; // Reset audio to the start
}
};

// Export function to play the alert sound
export const playAlertSound = () => {
    if (alertSound) {
    alertSound.play().catch((error) => {
        console.error('Audio play failed:', error);
    });
    }
};
