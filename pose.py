import mediapipe as mp
import cv2
from time import sleep
import keyboard
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
state = "down"
prevState = "down"
cap = cv2.VideoCapture(0)
# Initiate holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Make Detections
        results = holistic.process(image)
        rightElbow=results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ELBOW]
       
        if rightElbow.y>.73  :
            state = "down"
        if rightElbow.y<.7  :
            state = "up"

        
        if state=="down" and prevState=="up":
            print("EEE")
            keyboard.press("space")
            sleep(.01)
            keyboard.release("space")
 

        prevState=state

        # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
        
        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Draw face landmarks
      
        # Right hand
        #mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Left Hand
       # mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

        # Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
                        
        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
