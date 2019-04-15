


class ENT:
    
    def __init__(self, Game, id, pos):
        self.id = id
        self.pos = pos
        self.vel = [0, 0]
        self.physics = True
        self.model = "square.png"
        self.modelOffset = [-16, -16]
        
        Game.registerEntityHook(self, "keypress")
    
    def onTick(self, Game):
        Game.drawOffset = [
            -self.pos[0]+400,
            -self.pos[1]+300
        ]
    
    def onKey(self, Game, event):
        pygame = Game.pygame
        if event.key == pygame.K_w:
            self.vel[1] -= 1
        elif event.key == pygame.K_s:
            self.vel[1] += 1
        elif event.key == pygame.K_a:
            self.vel[0] -= 1
        elif event.key == pygame.K_d:
            self.vel[0] += 1
        elif event.key == pygame.K_SPACE:
            print(self.vel)
        
