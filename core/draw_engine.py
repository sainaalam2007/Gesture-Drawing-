import cv2

class DrawEngine:
    def __init__(self):
        self.prev_x, self.prev_y = 0, 0

    def draw(self, canvas, x, y, color):
        if self.prev_x == 0 and self.prev_y == 0:
            self.prev_x, self.prev_y = x, y

        cv2.line(canvas, (self.prev_x, self.prev_y), (x, y), color, 5)
        self.prev_x, self.prev_y = x, y

    def erase(self, canvas, x, y):
        cv2.circle(canvas, (x, y), 25, (0, 0, 0), -1)

    def reset(self):
        self.prev_x, self.prev_y = 0, 0