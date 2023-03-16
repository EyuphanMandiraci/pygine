import copy
from typing import Union

import pygame.draw

from pygine.math import Point2
from pygine.materials import Material
import threading


class Actor:
    def __init__(self, game, name: str, tag: str, position: Point2, material: Material,
                 size: Union[None, Point2] = None, autoCollide=True):
        self.name = name
        self.game = game
        self.tag = tag
        self.visible = True
        self.position = position
        self.first_position = position
        self.zIndex = 0
        self.autoCollide = autoCollide
        self.baseMaterial = material
        if self.baseMaterial.type == "Color":
            self.size = size
            self.baseMaterial.size = size
        else:
            self.size = self.baseMaterial.size
        self.baseMaterial.reinitSurface()
        self.material = self.baseMaterial.copy()
        self.surface = self.material.surface
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.position
        self.mask = None
        self.animations = {}
        self.animation = None
        # self._animThread = threading.Thread(target=self._animationLoop, daemon=True)
        self.animationPlaying = False
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
        self.animation.frame = 0
        if not self.animationPlaying:
            threading.Thread(target=self._animationLoop, daemon=True).start()
            self.animationPlaying = True

    def stopAnimation(self):
        self.animation = None
        self.material = self.baseMaterial.copy()
        self.material.reinitSurface()
        self.surface = self.material.surface.copy()
        self.animationPlaying = False

    def _animationLoop(self):
        while True:
            if self.animation is not None:
                self.animation.update()
            else:
                break

    def update(self):
        # self.position += self.current_velocity
        # self.current_velocity.force -= .057
        self.rect.topleft = self.position
        if self.rect.colliderect(self.game.scene.rect):
            self.visible = True
        else:
            self.visible = False
        if self.animation is not None:
            if self.animation.type == "Texture" and self.material.type == "Texture":
                self.material.reinitSurface(self.animation.frames[self.animation.frame]["image"])
                self.surface = self.material.surface
            elif self.animation.type == "Color" and self.material.type == "Color":
                self.material.reinitSurface(self.animation.frames[self.animation.frame]["color"])
                self.surface = self.material.surface
            else:
                self.stopAnimation()
        else:
            self.surface.blit(self.baseMaterial.surface, (0, 0))

        if self.autoCollide:
            self.mask = pygame.mask.from_surface(self.surface)

    def isCollide(self, other):
        if other.mask is not None:
            return self.mask.overlap(other.mask, other.position - self.position)

        return False



    def draw(self):
        self.game.scene.surface.blit(self.surface, self.position)
        self.surface.fill((0, 0, 0, 0))
