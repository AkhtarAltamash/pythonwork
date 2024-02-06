import cv2
import numpy as np

# Load pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier("C:/Users/Altamash Akhter/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Load pre-trained face recognition model (LBPH)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_recognition_model.yml")  # Load your trained model

# Open a connection to the default camera (usually the webcam)
video_cap = cv2.VideoCapture(0)

# Dictionary to map person IDs to names
person_dict = {0: "Altamash", 1: "Person2"}  # Add your own mappings

while True:
    # Read a frame from the video capture
    ret, frame = video_cap.read()

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection using Haar Cascade
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Extract the region of interest (ROI) from the grayscale frame
        face_roi = gray_frame[y:y + h, x:x + w]

        # Perform face recognition on the ROI
        label, confidence = face_recognizer.predict(face_roi)

        # Check if confidence is below a certain threshold (e.g., 100)
        if confidence < 100:
            person_name = person_dict.get(label, "Unknown")
        else:
            person_name = "Unknown"

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the person's name near the face
        cv2.putText(frame, person_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame with rectangles drawn around detected faces
    cv2.imshow("Face Recognition", frame)

    # Break the loop if the 'a' key is pressed
    if cv2.waitKey(10) == ord("a"):
        break

# Release the video capture object
video_cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
