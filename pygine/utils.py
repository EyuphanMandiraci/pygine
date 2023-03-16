import os
from reportlab.lib import colors


def getTexture(path):
    path_ = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "textures", path)
    return path_


def getAnimation(name):
    path_ = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "animations", f"{name}.json")
    path2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "animations")
    return path_, path2


def colorInterpolation(color1, color2, amount):
    if amount <= 1:
        return [color1]

    result = []
    for i in range(amount - 1):
        interpolated_color = colors.linearlyInterpolatedColor(
            colors.Color(*color1),
            colors.Color(*color2),
            0,
            amount - 1,
            i
        )
        result.append(interpolated_color)

    return result


def listChunker(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
