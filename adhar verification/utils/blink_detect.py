import cv2
import numpy as np
import mediapipe as mp
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, static_image_mode=False)

def calculate_ear(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

# Enhanced blink detector — tracks EAR only
def detect_blink(frame, threshold=0.2):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if not results.multi_face_landmarks:
        return False

    for face_landmarks in results.multi_face_landmarks:
        left_eye_indices = [362, 385, 387, 263, 373, 380]
        right_eye_indices = [33, 160, 158, 133, 153, 144]

        h, w = frame.shape[:2]

        left_eye = np.array([(int(face_landmarks.landmark[i].x * w),
                              int(face_landmarks.landmark[i].y * h)) for i in left_eye_indices])
        right_eye = np.array([(int(face_landmarks.landmark[i].x * w),
                               int(face_landmarks.landmark[i].y * h)) for i in right_eye_indices])

        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0

        return avg_ear < threshold  # True if eye is closed

    return False
