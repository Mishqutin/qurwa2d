


class ENT:

    def __init__(self, Game, id, pos):
        self.id = id
        self.pos = pos
        self.vel = [0, 0]
        self.physics = True
        self.model = "square.png"
        self.modelOffset = [-16, -16]

        Game.registerEntityHook(self, "tick")
        #Game.registerEntityHook(self, "keypress")

    def onTick(self, Game):
        Keys = Game.pygame.key.get_pressed()
        pygame = Game.pygame
        Game.drawOffset = [
            -self.pos[0]+400,
            -self.pos[1]+300
        ]


        force = self.vel

        if Keys[pygame.K_UP]:
            force[1] -= 0.3
        if Keys[pygame.K_DOWN]:
            force[1] += 0.3
        if Keys[pygame.K_LEFT]:
            force[0] -= 0.3
        if Keys[pygame.K_RIGHT]:
            force[0] += 0.3



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


    def speed(self):
        return math.sqrt(self.vel[0]**2 + self.vel[1]**2)
