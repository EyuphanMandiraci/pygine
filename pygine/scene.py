import pygame
from typing import List

from pygine.gui_components import BaseComponent


class Scene:
    def __init__(self, game, title):
        self.title: str = title
        self.surface: pygame.Surface = pygame.Surface((game.width, game.height), pygame.SRCALPHA)
        self.surface.fill((0, 0, 0, 0))
        self.game = game
        self.gui_components: List[BaseComponent] = self.defineComponents()
        self.actors: List = self.defineActors()

    def draw(self):
        for component in self.gui_components:
            component.draw()

        for actor in self.actors:
            actor.draw(self.surface)

        self.game.display.blit(self.surface, (0, 0))

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
