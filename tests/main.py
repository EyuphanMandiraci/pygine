import pygine
from MainMenu import MainMenu

window = pygine.Window(debug=True)
window.addScene("Main Menu", MainMenu(window))
window.setScene("Main Menu")
window.run()
