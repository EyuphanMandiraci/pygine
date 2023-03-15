import pygine.utils
from pygine import Actor
from pygine.gui_components import UIButton, UISlider, UICheckbox
from pygine.materials import ColorMaterial, TextureMaterial
from pygine.math import Point2, Point3
from pygine.scene import Scene
from pygine.input import Input
from pygine.animations import TextureAnimation, ColorAnimation


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game, "Main Menu")
        self.game = game

    def defineComponents(self):
        button = UIButton(self.game, self.surface, Point2(0, 100), text="Button", color=Point3(255, 0, 0), hoverColor=Point3(0, 255, 0))
        slider = UISlider(self.game, self.surface, Point2(0, 0), Point3(255, 255, 255), Point3(255, 0, 0), Point3(0, 255, 0), Point2(300, 20), 0, 100)
        checkbox = UICheckbox(self.game, self.surface, Point2(0, 50), Point3(255, 255, 255), Point2(20, 20))
        return [button, slider, checkbox]

    def defineActors(self):
        redMaterial = ColorMaterial("red", Point3(255, 0, 0))

        charMaterial = TextureMaterial("char", "headFocus.png")
        anim = TextureAnimation("walk")
        actor1 = Actor(self.game, "Actor 1", "actor1", Point2(100, 100), charMaterial)
        actor1.addAnimation(anim)
        actor1.playAnimation("walk")

        colorAnim = ColorAnimation("color", 1000)  # increase quality for better color animation
        actor2 = Actor(self.game, "Actor 2", "actor2", Point2(200, 200), redMaterial, Point2(100, 100))
        actor2.addAnimation(colorAnim)
        actor2.playAnimation("color")

        return [actor1, actor2]

    def update(self):
        super().update()
        if Input.isPressed("D"):
            self.getActor("Actor 1").position.x += 10 * self.game.deltaTime
        if Input.isPressed("A"):
            self.getActor("Actor 1").position.x -= 10 * self.game.deltaTime
        if Input.isPressed("W"):
            self.getActor("Actor 1").position.y -= 10 * self.game.deltaTime
        if Input.isPressed("S"):
            self.getActor("Actor 1").position.y += 10 * self.game.deltaTime


