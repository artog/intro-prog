__author__ = 'Adam'

import pygame as pg
from Game import Game
from Blocks import BlockShape,Block




pg.init()

screen_width = 400
screen_height = 700
screen = pg.display.set_mode([screen_width, screen_height])


done = True

blocks = []

currentBlock = Block(Game.lane[0])

blocks.append(currentBlock)
blo = Block()
game = Game(screen)
while not done:

    game.update()

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                currentBlock.shift(-1)
            if event.key == pg.K_RIGHT:
                currentBlock.shift(1)


    for block in blocks:
        block.update()

    for block in blocks:
        block.draw(screen)



    pg.display.flip()
