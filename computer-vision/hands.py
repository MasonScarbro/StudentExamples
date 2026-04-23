import cv2
import mediapipe as mp

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands() # Hands() = AI model that finds hand landmarks
mp_draw = mp.solutions.drawing_utils # drawing_utils = draws the skeleton (so technically its not needed but good for visualization)

# Each number = fingertip joint, Thumb is 4, index is 8, etc.
tip_ids = [4, 8, 12, 16, 20]

# This turns on the webcam
cap = cv2.VideoCapture(0)

# this is just the main video capture loop, it will run until you press 'q' to quit. It reads each frame, processes it to find hand landmarks, counts the fingers, and displays the result on the screen.
while True:
    success, img = cap.read()
    if not success:
        break

    # Flip for mirror effect
    img = cv2.flip(img, 1)

    '''
    Remember what we covered about computer vision? 
    AI models only understand numbers which is why
    computer vision models work with pixel values or RGB values.
    openCV uses BGR color format by default,
    but MediaPipe expects RGB. 
    So we need to convert the image before processing it with MediaPipe.
    '''
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # We are building off an already trained model so this just runs it
    results = hands.process(img_rgb)

    # this is storage for the state of each finger (1 for up, 0 for down)
    fingers = []

    if results.multi_hand_landmarks:

        # Most of this is just the drawing of the skeleton you see,\
        # again mainly just for visualization.
        # The important part is the logic for counting fingers which is below.
        for hand_landmarks in results.multi_hand_landmarks:

            # Draw landmarks
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            h, w, c = img.shape

            for lm in hand_landmarks.landmark:
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append((cx, cy))

            #BUG: This logic sometimes fails when hand is flipped, see if you can fix it?
            if landmarks[tip_ids[0]][0] > landmarks[tip_ids[0] - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other 4 fingers
            for i in range(1, 5):
                if landmarks[tip_ids[i]][1] < landmarks[tip_ids[i] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = sum(fingers)

            # display count
            cv2.putText(img, f'Fingers: {total_fingers}', (20, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

    cv2.imshow("Finger Counter", img) # shows you the camera

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()