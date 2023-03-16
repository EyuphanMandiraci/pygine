import pygine
from MainMenu import MainMenu

window = pygine.Window(debug=True, fps=60, fullscreen=False)
window.addScene("Main Menu", MainMenu(window))
window.setScene("Main Menu")
window.run()
