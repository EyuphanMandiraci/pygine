import os.path

import pygame

from pygine import utils
from pygine.animations import Animation
from PIL import Image
import time


class TextureAnimation(Animation):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Texture'
        self.imageName = self.properties['image']
        self.image = Image.open(os.path.join(utils.getAnimation(name)[1], self.imageName))
        self.imageWidth, self.imageHeight = self.image.size
        self.frameWidth = self.imageWidth
        self.frameHeight = self.imageHeight / self.frameCount
        self.parseFrames()

    def parseFrames(self):
        parsed = []
        for i in range(self.frameCount):
            cropped = self.image.crop((0, i * self.frameHeight, self.frameWidth, (i + 1) * self.frameHeight))
            parsed.append({
                "id": self.frames[i]["id"],
                "duration": self.frames[i]["duration"],
                "image": pygame.image.fromstring(
                    cropped.tobytes(),
                    cropped.size,
                    cropped.mode
                ).convert_alpha()
            })
        self.frames = parsed

    def update(self):
        if self.stopped:
            self.frame = 0
        if not self.paused:
            time.sleep(self.frames[self.frame]['duration'])
            self.frame += 1
            if self.frame >= len(self.frames):
                self.frame = 0
