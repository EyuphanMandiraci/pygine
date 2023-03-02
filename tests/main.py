import pygine
from MainMenu import MainMenu

window = pygine.Window(debug=True)
window.addScreen("Main Menu", MainMenu(window))
window.setScreen("Main Menu")
window.run()
