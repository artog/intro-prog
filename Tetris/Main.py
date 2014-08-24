__author__ = 'Adam'

import pygame as pg


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)


class Block(pg.sprite.Sprite):
    image = None
    rect = None
    speed = 1

    def __init__(self,x=0,y=0):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([20,20])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.center = (y,x)

    def update(self):
        self.rect.centery += 0.6*self.speed


class BlockShape(object):

    blocks = []
    shape = [[0,0,1,0],
             [0,1,1,0],
             [0,1,0,0],
             [0,0,0,0]]

    def __init__(self):
        b = Block()
        self.blocks.append(b)

    def draw(self,screen):
        for block in self.blocks:
            screen.blit(block.image,block.rect)
        pass
    def update(self):
        for block in self.blocks:
            block.update()

pg.init()

screen_width = 400
screen_height = 700
screen = pg.display.set_mode([screen_width, screen_height])


done = False

blocks = []

testBlock = BlockShape()

blocks.append(testBlock)
blo = Block()
while not done:
    screen.fill(WHITE)
    pg.draw.line(screen,BLACK,( 75,  0),(75,650))
    for i in range(9):
        pg.draw.line(screen,BLACK,(100+25*i,  0),(100+25*i,650))
    pg.draw.line(screen,BLACK,( 325,  0),(325,650))
    pg.draw.line(screen,BLACK,( 75,650),(325,650))
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            done = True


    for block in blocks:
        block.update()

    for block in blocks:
        block.draw(screen)



    pg.display.flip()