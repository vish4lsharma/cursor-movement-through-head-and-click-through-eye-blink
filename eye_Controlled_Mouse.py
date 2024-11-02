import cv2
import pyautogui
import numpy as np

# Load Haar Cascades for face and eyes
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set screen size for cursor movement
screen_width, screen_height = pyautogui.size()

# Variables for eye blink detection
blink_counter = 0
eye_blink_threshold = 3  # Frames without detecting eyes to trigger a blink
blinked = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video")
        break

    # Convert the frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        # Process the first detected face
        (x, y, w, h) = faces[0]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Detect eyes within the face region
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Eye blink detection logic
        if len(eyes) == 0:  # No eyes detected
            blink_counter += 1
            if blink_counter > eye_blink_threshold and not blinked:  
                pyautogui.click()  # Click action on blink
                blinked = True  # Set blinked to True to prevent multiple clicks
        else:
            if blinked:  
                blinked = False  # Reset blinked if eyes are detected again
            blink_counter = 0  # Reset blink counter if eyes are detected

        # Draw rectangles around detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # Move the cursor based on face position
        # Calculate the center of the detected face
        center_x = x + w // 2
        center_y = y + h // 2
        
        # Normalize the face center to screen size
        screen_x = np.interp(center_x, [0, frame.shape[1]], [0, screen_width])
        screen_y = np.interp(center_y, [0, frame.shape[0]], [0, screen_height])

        # Move the cursor
        pyautogui.moveTo(screen_x, screen_y)

    # Show the processed frame
    cv2.imshow('Head Movement Control', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
