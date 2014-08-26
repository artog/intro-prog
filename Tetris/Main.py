__author__ = 'Adam'

import pygame as pg
from Game import Game
from Blocks import BlockShape,Block




pg.init()

screen_width = 400
screen_height = 700
screen = pg.display.set_mode([screen_width, screen_height])


done = False

blocks = []

currentBlock = BlockShape(Game.lane[1])

# blocks.append(currentBlock)
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

    if len(pg.sprite.spritecollide(currentBlock,blocks,False)) > 0:
        currentBlock.stop()

    # for block in blocks:
    #     block.update()
    currentBlock.update()
    print(currentBlock.rect.bottom)
    if currentBlock.rect.bottom+1 >= 650:
        b = currentBlock.stop()
        currentBlock = BlockShape(Game.lane[2])
        blocks.append(b)
    for block in blocks:
        block.draw(screen)

    currentBlock.draw(screen)



    pg.display.flip()
