class tile:

    def __init__(self, bottom=None, top=None):
        self.dirty = 1
        self.bottomsprite = bottom
        self.topsprite = top

    def set_topsprite(self, sprite):
        self.topsprite = sprite
        self.dirty = 1

    def get_topsprite(self):
        return self.topsprite

    def set_bottomsprite(self, sprite):
        self.bottomsprite = sprite
        self.dirty = 1

    def get_bottomsprite(self):
        return self.bottomsprite

    def blit(self, screen, coords, all=False):
        if all or self.dirty:
            if self.bottomsprite != None:
                screen.blit(self.bottomsprite,coords)
            if self.topsprite != None:
                screen.blit(self.topsprite,coords)
            self.dirty = 0
            return True
        else:
            return False
