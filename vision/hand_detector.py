import cv2
import mediapipe as mp

class GestureVision:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.results = None

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)

    def get_points(self, frame):
        points = []
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                for idx, lm in enumerate(hand.landmark):
                    h, w, _ = frame.shape
                    x, y = int(lm.x * w), int(lm.y * h)
                    points.append((idx, x, y))
        return points