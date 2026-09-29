def detect_gesture(points):
    if not points:
        return "none"

    tips = [8, 12, 16, 20]
    fingers = []

    fingers.append(1 if points[4][1] > points[3][1] else 0)

    for tip in tips:
        fingers.append(1 if points[tip][2] < points[tip-2][2] else 0)

    total = sum(fingers)

    if total == 1:
        return "draw"
    elif total == 2:
        return "color"
    elif total >= 4:
        return "erase"
    elif total == 0:
        return "clear"
    else:
        return "idle"