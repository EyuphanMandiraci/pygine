import pygame

from pygine.shape_settings import ShapeSettings
from pygine.materials import Material


class ColorMaterial(Material):
    def __init__(self, name, color, shape: ShapeSettings):
        super().__init__(name)
        self.color = color
        self.size = (1, 1)
        self.shape = shape
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)
        self.surface = self.surface.convert()
        self.type = "Color"

    def reinitSurface(self, color=None):
        if color is not None:
            self.color = (color.red, color.green, color.blue)
        self.surface = pygame.Surface(self.size).convert()
        self.surface.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        if self.shape.shape == "circle":
            pygame.draw.ellipse(self.surface, self.color, (0, 0, self.size[0], self.size[1]), self.shape.border_width if not self.shape.fill and self.shape.border_width is not None else 0)
        elif self.shape.shape == "square":
            pygame.draw.rect(self.surface, self.color, (0, 0, self.size[0], self.size[1]), self.shape.border_width if not self.shape.fill and self.shape.border_width is not None else 0)

    def copy(self):
        copy = ColorMaterial(self.name, self.color, self.shape)
        copy.type = self.type
        copy.surface = self.surface
        copy.size = self.size
        return copy

