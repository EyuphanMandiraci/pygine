import pygame

from pygine.gui_components import BaseComponent
from pygine import math


class UISlider(BaseComponent):
    def __init__(self,
                 game,
                 parentSurface,
                 position,
                 color,
                 cursorColor,
                 activeColor,
                 size,
                 minVal,
                 maxVal):
        super().__init__(game, parentSurface, position, color, size)
        self.cursorColor = cursorColor
        self.activeColor = activeColor
        self.minVal = minVal
        self.maxVal = maxVal
        self.value = minVal
        self.selectorRect = pygame.Rect(
            self.position[0],
            self.position[1],
            self.size[0] / 10,
            self.size[1]
        )
        self.onValueChanged = []

    def draw(self):
        self.surface.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surface, self.color, self.rect, 0, 10)
        pygame.draw.rect(self.surface, self.activeColor, pygame.Rect(
            self.rect.x,
            self.rect.y,
            self.selectorRect.x - self.rect.x + self.selectorRect.width,
            self.rect.height
        ), 0, 10)
        pygame.draw.ellipse(self.surface, self.cursorColor, self.selectorRect, 0)
        super().draw()

    def triggerOnClick(self, evt=None):
        self.clicked = True
        self.triggerOnDrag(evt)
        super().triggerOnClick(evt)

    def triggerOnDrag(self, evt=None):
        if evt.pos[0] < self.rect.x:
            self.selectorRect.x = self.rect.x
        elif evt.pos[0] > self.rect.x + self.rect.width - self.selectorRect.width:
            self.selectorRect.x = self.rect.x + self.rect.width - self.selectorRect.width
        else:
            self.selectorRect.x = evt.pos[0]

        self.value = math.utils.interpolate(self.rect.x, self.rect.x + self.rect.width - self.selectorRect.width, self.minVal, self.maxVal, self.selectorRect.x)
        for event in self.onValueChanged:
            event(self.value)
        super().triggerOnDrag(evt)