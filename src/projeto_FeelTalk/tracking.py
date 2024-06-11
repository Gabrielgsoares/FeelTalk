import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Inicialização da câmera e bibliotecas
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Defina o fator de sensibilidade (quanto maior, mais sensível)
sensitivity = 7.5

# Inicializar o cursor no meio da tela
pyautogui.moveTo(screen_w / 2, screen_h / 2)

# Parâmetros para a média móvel
history_length = 5
x_history = []
y_history = []

def moving_average(values, new_value, length):
    values.append(new_value)
    if len(values) > length:
        values.pop(0)
    return np.mean(values)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                # Calcular o deslocamento relativo a partir do centro da tela da câmera
                screen_x = screen_w / 2 + (landmark.x - 0.5) * screen_w * sensitivity
                screen_y = screen_h / 2 + (landmark.y - 0.5) * screen_h * sensitivity
                
                # Aplicar média móvel
                screen_x = moving_average(x_history, screen_x, history_length)
                screen_y = moving_average(y_history, screen_y, history_length)
                
                # Garantir que as coordenadas estejam dentro dos limites da tela
                screen_x = min(screen_w, max(0, screen_x))
                screen_y = min(screen_h, max(0, screen_y))
                pyautogui.moveTo(screen_x, screen_y)
        
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    
    #cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
