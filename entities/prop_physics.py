


class ENT:
    test = "hello"
    def __init__(self, Game, id, pos):
        self.id = id
        self.pos = pos
        self.vel = [0, 0]
        self.physics = True
        self.model = "square.png"
        self.modelOffset = [0, 0]
    
    def onTick(self, Game):
        pass