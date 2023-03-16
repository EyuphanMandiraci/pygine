import pygame
from typing import List

from pygine.gui_components import BaseComponent


class Scene:
    def __init__(self, game, title):
        self.title: str = title
        self.surface: pygame.Surface = pygame.Surface((game.width, game.height), pygame.SRCALPHA).convert_alpha()
        self.surface.fill((0, 0, 0, 0))
        self.rect = self.surface.get_rect()
        self.game = game
        self.gui_components: List[BaseComponent] = self.defineComponents()
        self.actors: List = self.defineActors()

    def draw(self):
        zIndexSorted = self.gui_components + self.actors
        zIndexSorted = sorted(zIndexSorted, key=lambda x: x.zIndex)
        for item in zIndexSorted:
            if item.visible:
                item.draw()

        self.game.display.blit(self.surface, (0, 0))
        self.surface.fill((0, 0, 0, 0))

    def update(self):
        mouse = pygame.mouse
        for component in self.gui_components:
            if component.rect.collidepoint(mouse.get_pos()):
                if not component.hovered:
                    component.hovered = True
                    component.triggerOnHover(mouse)
            else:
                if component.hovered:
                    component.hovered = False
                    component.triggerOnLeave(mouse)
            component.update()

        for actor in self.actors:
            actor.update()

    def defineComponents(self):
        return []

    def defineActors(self):
        return []

    def getActor(self, name):
        for actor in self.actors:
            if actor.name == name:
                return actor
        return None

