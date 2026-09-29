import cv2
import numpy as np
from vision.hand_detector import GestureVision
from logic.gesture_control import detect_gesture
from core.draw_engine import DrawEngine

cap = cv2.VideoCapture(0)

detector = GestureVision()
drawer = DrawEngine()

canvas = np.zeros((480, 640, 3), dtype=np.uint8)
history = []

colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
current_color = colors[0]

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    detector.process(frame)
    points = detector.get_points(frame)
    gesture = detect_gesture(points)

    for i, col in enumerate(colors):
        cv2.rectangle(frame, (i*100,0), ((i+1)*100,50), col, -1)

    if points:
        x, y = points[8][1], points[8][2]

        if gesture == "draw":
            history.append(canvas.copy())
            drawer.draw(canvas, x, y, current_color)

        elif gesture == "erase":
            history.append(canvas.copy())
            drawer.erase(canvas, x, y)

        elif gesture == "clear":
            history.append(canvas.copy())
            canvas = np.zeros_like(canvas)

        elif gesture == "color":
            if y < 50:
                index = x // 100
                if index < len(colors):
                    current_color = colors[index]

        else:
            drawer.reset()

    output = cv2.addWeighted(frame, 0.7, canvas, 0.7, 0)

    cv2.imshow("Gesture Draw", output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        cv2.imwrite("my_drawing.png", canvas)

    elif key == ord('u'):
        if history:
            canvas = history.pop()

    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()