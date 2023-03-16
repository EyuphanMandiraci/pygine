class Material:
    def __init__(self, name):
        self.name = name
        self.type = "Empty"
        self.surface = None
        self.size = None

    def reinitSurface(self, image=None):
        pass

    def copy(self):
        copy = Material(self.name)
        copy.type = self.type
        copy.surface = self.surface
        copy.size = self.size
        return copy
