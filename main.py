import pygame
from game import gameClass




Game = gameClass.game()

Game.loadModel("square.png")
Game.loadModel("bush.png")
Game.loadEntity("prop_physics.py", "prop_physics")
Game.loadEntity("ent_chuj.py", "ent_chuj")
Game.loadEntity("prop_static.py", "prop_static")

lol = Game.createEntity("prop_physics", [500, 500])
lol.vel = [-1, -1]

ent = Game.createEntity("prop_static", [500, 500])
ent.model = "bush.png"
ent = Game.createEntity("prop_static", [700, 400])
ent.model = "bush.png"
ent = Game.createEntity("prop_static", [200, 100])
ent.model = "bush.png"
ent = Game.createEntity("prop_static", [100, 400])
ent.model = "bush.png"
ent = Game.createEntity("prop_static", [300, 400])
ent.model = "bush.png"

chuj = Game.createEntity("ent_chuj", [500, 500])

x, y, i = Game.mapStoreEntity(lol)
print(x, y, i)
Game.mapRestoreEntity(0, 0, 0)

while Game.running:
    Game.main()




