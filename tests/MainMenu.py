from pygine.gui_components import UIButton, UISlider, UICheckbox
from pygine.math import Point2, Point3
from pygine.scene import Scene


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game, "Main Menu")
        self.game = game

    def defineComponents(self):
        button1 = UIButton(
            self.game,
            position=Point2(self.game.width / 2 - 100, self.game.height / 2 - 50),
            color=Point3(255, 0, 0),
            hoverColor=Point3(0, 255, 0),
            text="Play",
            font="Arial",
            fontSize=32,
            textColor=Point3(0, 0, 0),
            size=Point2(200, 100),
            parentSurface=self.surface
        )
        slider1 = UISlider(
            self.game,
            position=Point2(0, 0),
            color=Point3(255, 0, 0),
            cursorColor=Point3(0, 255, 0),
            activeColor=Point3(0, 0, 255),
            size=Point2(250, 25),
            minVal=0,
            maxVal=100,
            parentSurface=self.surface
        )
        checkbox1 = UICheckbox(
            self.game,
            position=Point2(0, 50),
            color=Point3(255, 0, 0),
            size=Point2(25, 25),
            parentSurface=self.surface
        )
        checkbox1.onValueChange.append(lambda val: print(val))
        return [button1, slider1, checkbox1]
