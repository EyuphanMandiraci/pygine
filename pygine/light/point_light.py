import pygame
import pygame.gfxdraw

from pygine import utils
from PIL import Image

class PointLight:
    def __init__(self, game, position, color, power):
        self.game = game
        self.position = position
        self.color = color
        self.power = power * 5
        self.surface = pygame.Surface((self.power, self.power), pygame.SRCALPHA)
        self.circle = pygame.Surface((self.power, self.power), pygame.SRCALPHA)
        self.colors = utils.colorInterpolation((color[0], color[1], color[2], 255), (color[0], color[1], color[2], 0),
                                               self.power)
        self.colors = [(255 - color.red, 255 - color.green, 255 - color.blue, 255 - color.alpha) for color in self.colors]
        self.zIndex = 9999
        self.visible = True

    def draw(self):
        self.surface.fill((0, 0, 0, 0))
        for power, color in zip(range(self.power, 0, -1), self.colors):
            pygame.gfxdraw.filled_ellipse(self.surface, self.surface.get_rect().centerx, self.surface.get_rect().centery, power // 2, power // 2, color)
        self.game.scene.light_surface.blit(self.surface, (self.position[0], self.position[1]))


