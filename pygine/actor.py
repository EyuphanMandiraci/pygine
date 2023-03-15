import copy
from typing import Union

import pygame.draw

from pygine.math import Point2
from pygine.materials import Material
import threading


class Actor:
    def __init__(self, game, name: str, tag: str, position: Point2, material: Material,
                 size: Union[None, Point2] = None):
        self.name = name
        self.game = game
        self.tag = tag
        self.position = position
        self.first_position = position
        self.material = material
        if self.material.type == "Color":
            self.size = size
            self.material.size = size
        else:
            self.size = self.material.size
        self.material.reinitSurface()
        self.surface = self.material.surface
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.position
        self.animations = {}
        self.animation = None
        self._animThread = threading.Thread(target=self._animationLoop, daemon=True)
        # self._velocity = Vector2(self.position, 0, 0)
        # self.current_velocity = copy.deepcopy(self._velocity)

    # @property
    # def velocity(self):
    #     return self._velocity
    #
    # @velocity.setter
    # def velocity(self, value):
    #     self._velocity = value
    #     self.current_velocity = copy.deepcopy(self._velocity)

    def addAnimation(self, animation):
        self.animations[animation.name] = animation

    def playAnimation(self, name):
        self.animation = self.animations.get(name)
        self._animThread.start()

    def _animationLoop(self):
        while True:
            if self.animation is not None:
                self.animation.update()

    def update(self):
        # self.position += self.current_velocity
        # self.current_velocity.force -= .057
        self.rect.topleft = self.position
        if self.animation is not None:
            if self.animation.type == "Texture" and self.material.type == "Texture":
                self.material.reinitSurface(self.animation.frames[self.animation.frame]["image"])
                self.surface = self.material.surface
            elif self.animation.type == "Color" and self.material.type == "Color":
                self.material.reinitSurface(self.animation.frames[self.animation.frame]["color"])
                self.surface = self.material.surface

    def draw(self):
        self.game.scene.surface.blit(self.surface, self.position)
