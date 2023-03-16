import time

from pygine import utils
from pygine.animations import Animation


class ColorAnimation(Animation):
    def __init__(self, name, quality=50):
        super().__init__(name)
        self.type = 'Color'
        self.fromColor = self.properties["fromColor"]
        self.toColor = self.properties["toColor"]
        self.quality = quality
        self.createFrames()

    def createFrames(self):
        colors = utils.colorInterpolation(self.fromColor, self.toColor, self.quality)
        self.frames = []
        for i in range(len(colors)):
            self.frames.append({
                "id": i,
                "duration": self.properties["duration"] / 1000 / len(colors),
                "color": colors[i]
            })

    def update(self):
        if self.stopped:
            self.frame = 0
        if not self.paused:
            time.sleep(self.frames[self.frame]['duration'])
            self.frame += 1
            if self.frame >= len(self.frames):
                self.frame = 0




