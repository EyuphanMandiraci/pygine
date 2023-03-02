import time

import screeninfo
import pygame
import sys
from pygine import math as pmath
from typing import Union
import math

pygame.init()


class Window:
    def __init__(self,
                 title: str = "Pygine",
                 size: Union[None, pmath.Point2] = pmath.Point2(800, 600),
                 fps: Union[None, int] = None,
                 background_color: pmath.Point3 = pmath.Point3(0, 0, 0),
                 fullscreen: bool = False,
                 debug: bool = False):
        self.monitor: screeninfo.Monitor = screeninfo.get_monitors()[0]
        self.width: int = self.monitor.width if fullscreen else size[0]
        self.height: int = self.monitor.height if fullscreen else size[1]
        self.title: str = title
        self.background_color: pmath.Point3 = background_color
        self.fps: Union[None, int] = fps
        self.mainloop: bool = True
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.deltaTime: float = 0
        self.__startTime: float = time.time()
        self.display: Union[None, pygame.Surface] = None
        self.debug: bool = debug
        self.screens = {}
        self.screen = None
        self.initWindow(self.title, pmath.Point2(self.width, self.height), fullscreen)

    def initWindow(self,
                   title: str,
                   size: pmath.Point2,
                   fullscreen: bool):
        pygame.display.set_caption(title)
        surf = pygame.surface.Surface((1, 1), pygame.SRCALPHA)
        surf.fill((0, 0, 0, 1))
        pygame.display.set_icon(surf)
        if fullscreen:
            self.display = pygame.display.set_mode(size, pygame.FULLSCREEN | pygame.DOUBLEBUF)
        else:
            self.display = pygame.display.set_mode(size, pygame.DOUBLEBUF)

    def update(self):
        if self.screen is not None:
            self.screen.update()

    def draw(self):
        if self.screen is not None:
            self.screen.draw()
        if self.debug:
            self.__drawDebug()

    def __drawDebug(self):
        font = pygame.font.SysFont("Arial", 16)
        text = font.render(f"FPS: {int(self.clock.get_fps())}", True, (0, 255, 0))
        self.display.blit(text, (self.width - text.get_width(), 0))

    def addScreen(self, name, screen):
        self.screens[name] = screen

    def setScreen(self, name):
        self.screen = self.screens[name]

    def run(self):
        while self.mainloop:
            current: float = time.time()
            self.deltaTime = pmath.utils.calculateDeltaTime(self.__startTime, current)
            self.__startTime = current
            self.update()
            pygame.event.set_allowed([pygame.QUIT])
            if self.fps is None:
                self.clock.tick()
            else:
                self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for component in self.screen.gui_components:
                        if component.rect.collidepoint(event.pos):
                            component.triggerOnClick(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    for component in self.screen.gui_components:
                        if component.clicked:
                            component.triggerOnRelease(event)
                if event.type == pygame.MOUSEMOTION:
                    for component in self.screen.gui_components:
                        if component.clicked:
                            component.triggerOnDrag(event)
            self.display.fill(self.background_color)
            self.draw()
            pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()
