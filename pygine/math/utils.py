def calculatePercentage(value, percentage, isInt=False):
    if isInt:
        return int(value * (percentage / 100))
    return value * (percentage / 100)


def interpolate(x1, x2, y1, y2, x):
    return (y2 - y1) * (x - x1) / (x2 - x1) + y1


def calculateDeltaTime(lastTime, currentTime):
    return (currentTime - lastTime) * 60


