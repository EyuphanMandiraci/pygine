class Material:
    def __init__(self, name):
        self.name = name
        self.type = "Empty"
        self.surface = None
        self.size = None

    def reinitSurface(self, image=None):
        pass