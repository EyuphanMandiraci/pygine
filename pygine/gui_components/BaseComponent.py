from typing import List, Union

import pygame

from pygine import math


class BaseComponent:
    def __init__(self,
                 game,
                 parentSurface,
                 position: math.Point2,
                 color: math.Point3,
                 size:  Union[math.Point2, List[str]] = math.Point2(100, 100)
                 ):
        self.position: math.Point2 = position
        if isinstance(size, list):
            self.size = math.Point2(
                int(math.utils.calculatePercentage(int(size[0].replace("%")), parentSurface.get_width(), True)),
                int(math.utils.calculatePercentage(int(size[1].replace("%")), parentSurface.get_height(), True))
            )
        else:
            self.size = size
        self.color: math.Point3 = color
        self.game = game
        self.surface: pygame.Surface = pygame.Surface((self.size[0], self.size[1]), pygame.SRCALPHA)
        self.surface.fill((0, 0, 0, 0))
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.onClick = []
        self.onRelease = []
        self.onHover = []
        self.onLeave = []
        self.onDrag = []
        self.clicked = False
        self.hovered = False
        self.parentSurface = parentSurface

    def draw(self):
        self.parentSurface.blit(self.surface, self.position)

    def update(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def triggerOnClick(self, evt=None):
        self.clicked = True
        for event in self.onClick:
            event()

    def triggerOnRelease(self, evt=None):
        self.clicked = False
        for event in self.onRelease:
            event()

    def triggerOnHover(self, evt=None):
        self.hovered = True
        for event in self.onHover:
            event()

    def triggerOnLeave(self, evt=None):
        self.hovered = False
        for event in self.onLeave:
            event()

    def triggerOnDrag(self, evt=None):
        for event in self.onDrag:
            event()
