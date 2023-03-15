import pygame

from pygine import utils
from pygine.materials import Material


class TextureMaterial(Material):
    def __init__(self, name: str, texture: str):
        super().__init__(name)
        self.path = utils.getTexture(texture)
        self.type = "Texture"
        self.image = None
        self.shown = False
        self.reinitSurface()

    def reinitSurface(self, image=None):
        if image is not None:
            self.image = image
        else:
            self.image = pygame.image.load(self.path)
        if self.image.get_alpha():
            self.image = self.image.convert_alpha()
        else:
            self.image = self.image.convert()
        self.size = self.image.get_size()
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA if self.image.get_alpha() else 0)
        self.surface.blit(self.image, (0, 0))
        self.surface = self.surface.convert_alpha()

