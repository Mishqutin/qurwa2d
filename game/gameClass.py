import pygame
import time
import math


class game:

    def __init__(self):
        self.running = True

        self.Resources = {
            "models": {},
            "entities": {},
        }
        self.Entities = []
        self.EntHooks = {
            "tick": [],
            "keypress": []
        }

        # Map.
        self.Map = {}
        self.mapInit()

        # Drawing.
        self.bgColor = (255, 255, 255)
        self.colorkey = (255, 255, 255)

        self.drawOffset = [0, 0]

        # Physics.
        self.physFriction = 0.08

        # Game.
        self.resolution = (800, 600)
        self.ltick = 0
        self.tickdelay = 0.015


        self.pygame = pygame

        # Init.
        pygame.init()

        # Title.
        self.title = "Qurwa Flat engine                                                              (C) Mishqutin Ltd.                                                        \"Jebać psy\""
        pygame.display.set_caption(self.title)

        # Icon.
        self.icon = pygame.image.load("./icon.png")
        pygame.display.set_icon(self.icon)

        # Resolution
        self.screen = pygame.display.set_mode(self.resolution)
        # Font
        self.myFont = pygame.font.SysFont("arial", 25)

        self.screen.set_colorkey(self.colorkey)


        self.introLogo = pygame.image.load("./intro.png")
        self.introLogo.set_colorkey(self.colorkey)
        self.intro()


    def intro(self):
        """Intro sequence."""
        img = self.introLogo

        for i in range(155):
            self.screen.fill((60, 40, 40))
            img.set_alpha(i+100)
            self.screen.blit(img, (200, 200))
            pygame.display.flip()
            time.sleep(0.005)

        text = "\"Pora wypierdalać z rynku.\"  ~Ja"

        for i in range(100):
            self.screen.fill((60, 40, 40))
            self.screen.blit(img, (200, 200))
            i+=100
            label = self.myFont.render(text, True, (i, i, i))
            self.screen.blit(label, (300, 450))
            pygame.display.flip()
            time.sleep(0.01)
        #time.sleep(0.2)


    # LOOP FUNCTIONS =======
    def main(self):
        ctime = time.time()
        if ctime - self.ltick < self.tickdelay: return None
        self.ltick = ctime

        self.events()
        self.physics()
        self.draw()

    def events(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LALT] and keys[pygame.K_F4]:
            self.running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                for ent in self.EntHooks["keypress"]:
                    ent.onKey(self, event)

        for ent in self.EntHooks["tick"]:
            ent.onTick(self)


    def physics(self):
        for ent in self.Entities:
            if not ent: continue
            if not ent.physics: continue

            sx, sy = ent.vel
            x, y   = ent.pos

            x += sx
            y += sy

            msx = abs(sx)-self.physFriction
            msy = abs(sy)-self.physFriction

            if msx<=0: msx = 0
            else: msx = math.copysign(msx, sx)

            if msy<=0: msy = 0
            else: msy = math.copysign(msy, sy)

            ent.pos = [x, y]
            ent.vel = [msx, msy]


    def draw(self):
        self.screen.fill(self.bgColor)

        for ent in self.Entities:
            if not ent: continue
            if not ent.model: continue
            pos = ent.pos
            offX = self.drawOffset[0] + ent.modelOffset[0]
            offY = self.drawOffset[1] + ent.modelOffset[1]
            posNorm = (
                int(pos[0])+offX,
                int(pos[1])+offY
            )

            imgName = ent.model
            img = self.Resources["models"][imgName]
            self.screen.blit(img, posNorm)

        pygame.display.flip()
    # ========================


    # Load resources
    def loadModel(self, path):
        img = pygame.image.load("./images/"+path)
        img.set_colorkey(self.colorkey)
        self.Resources["models"][path] = img


    def loadEntity(self, path, name):
        f = open("./entities/"+path)
        code = f.read()
        f.close()

        execLocals = {"ENT": None}
        exec(code, globals(), execLocals)

        ent = execLocals["ENT"]
        self.Resources[name] = ent

        if hasattr(ent, "test"):
            print(ent.test)

    # Create ents
    def createEntity(self, name, pos=[0,0]):
        id = len(self.Entities)
        ent = self.Resources[name](self, id, pos)
        self.Entities.append(ent)

        return self.Entities[id]

    def removeEntity(self, ent):
        id = ent.id
        self.Entities[id] = None

    # Hooks
    def registerEntityHook(self, ent, name):
        self.EntHooks[name].append(ent)

    # Map
    def mapInit(self):
        for x in range(4):
            self.Map[ x] = {}
            self.Map[-x] = {}
            for y in range(4):
                self.Map[ x][ y] = []
                self.Map[-x][ y] = []
                self.Map[ x][-y] = []
                self.Map[-x][-y] = []

    def mapStoreEntity(self, ent):
        x, y = ent.pos
        x, y = int(x), int(y)
        mx, my = int(x/2048), int(y/2048)
        self.Map[mx][my].append(ent)

        self.removeEntity(ent)

        return mx, my, None

    def mapRestoreEntity(self, x, y, i):
        ent = self.Map[x][y][i]
        del self.Map[x][y][i]
        id = len(self.Entities)
        self.Entities.append(ent)
        ent.id = id
