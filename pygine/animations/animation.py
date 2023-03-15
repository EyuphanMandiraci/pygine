import json
from pygine import utils


class Animation:
    def __init__(self, name):
        self.name = name
        self.type = None
        self.properties = json.load(open(utils.getAnimation(name)[0], 'r'))
        self.frames = self.properties.get('frames', [])
        self.frameCount = len(self.frames)
        self.frame = 0
        self.paused = False
        self.stopped = False

    def update(self):
        pass

    def getFrame(self):
        return self.frames[self.frame]
