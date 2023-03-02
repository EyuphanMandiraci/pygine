import pygame

from pygine.gui_components import BaseComponent
from pygine import math


class UIButton(BaseComponent):
    def __init__(self,
                 game,
                 parentSurface,
                 position: math.Point2 = math.Point2(0, 0),
                 color: math.Point3 = math.Point3(0, 0, 0),
                 hoverColor: math.Point3 = math.Point3(0, 0, 0),
                 text: str = "",
                 font: str = "Arial",
                 fontSize: int = 16,
                 textColor: math.Point3 = math.Point3(0, 0, 0),
                 size: math.Point2 = math.Point2(100, 100)
                 ):
        super().__init__(game, parentSurface, position, color, size)
        self.hoverColor = hoverColor
        self.text = text
        self.font = font
        self.fontSize = fontSize
        self.textColor = textColor
        self.font = pygame.font.SysFont(self.font, self.fontSize)

    def draw(self):
        if self.hovered:
            self.surface.fill(self.hoverColor)
        else:
            self.surface.fill(self.color)
        if self.text != "":
            text = self.font.render(self.text, True, self.textColor)
            self.surface.blit(text, (self.size[0] / 2 - text.get_width() / 2, self.size[1] / 2 - text.get_height() / 2))
        self.parentSurface.blit(self.surface, self.position)

