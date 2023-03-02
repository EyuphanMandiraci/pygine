from typing import Union, List

import pygame

from pygine import math
from pygine.gui_components import BaseComponent


class UICheckbox(BaseComponent):
    def __init__(self,
                 game,
                 parentSurface,
                 position: math.Point2,
                 color: math.Point3,
                 size: Union[math.Point2, List[str]] = math.Point2(100, 100)
                 ):
        super().__init__(game, parentSurface, position, color, size)
        self.checked = False
        self.onValueChange = []

    def draw(self):
        self.surface.fill((0, 0, 0, 255))
        if self.checked:
            pygame.draw.rect(self.surface, self.color, (0, 0, self.size[0], self.size[1]))
        else:
            pygame.draw.rect(self.surface, self.color, (0, 0, self.size[0], self.size[1]), 1)
        super().draw()

    def triggerOnClick(self, evt=None):
        self.checked = not self.checked
        for event in self.onValueChange:
            event(self.checked)
        super().triggerOnClick(evt)