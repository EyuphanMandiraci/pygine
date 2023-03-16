import pygame

from pygine.materials import Material


class ColorMaterial(Material):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.size = (1, 1)
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)
        self.surface = self.surface.convert()
        self.type = "Color"

    def reinitSurface(self, color=None):
        if color is not None:
            self.color = (color.red, color.green, color.blue)
        self.surface = pygame.Surface(self.size).convert()
        self.surface.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.surface.fill(self.color)

    def copy(self):
        copy = ColorMaterial(self.name, self.color)
        copy.type = self.type
        copy.surface = self.surface
        copy.size = self.size
        return copy

