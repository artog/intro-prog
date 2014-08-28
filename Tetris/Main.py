__author__ = 'Adam'

import pygame as pg
from Game import Game


pg.init()

screen_width = 400
screen_height = 700
screen = pg.display.set_mode([screen_width, screen_height])


done = False

blocks = []

# blocks.append(currentBlock)
game = Game(screen)
while not game.isDone():

    game.update()

    game.handleEvents()

    pg.display.flip()
