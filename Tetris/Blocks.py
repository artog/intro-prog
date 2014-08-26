__author__ = 'iadam'

import Colors
import pygame as pg

class BlockShape(object):

    blocks = []
    shape = [[1]]
    position = [0,0]
    rect = pg.Rect(0,0,1,1)

    def __init__(self,lane):
        b = Block(lane)
        self.blocks.append(b)
        self.calcRect()

    def calcRect(self):
        top = 1000000
        left = 1000000
        bottom = 0
        right = 0
        for block in self.blocks:
            if block.rect.x < left:
                left = block.rect.x
            if block.rect.y < top:
                top = block.rect.y
            if block.rect.bottom > bottom:
                bottom = block.rect.bottom
            if block.rect.right > right:
                right = block.rect.right
        self.rect = pg.Rect(
            left,
            top,
            right-left,
            bottom-top
        )

    def draw(self,screen):
        for block in self.blocks:
            block.draw(screen)

    def update(self):
        for block in self.blocks:
            block.update()
        self.calcRect()

    def rotate(self):
        r = []
        for i in range(len(self.shape[0])):
            r.append([])
            for j in range(len(self.shape)):
                r[-1].append(self.shape[j][i])
        self.shape = r

    def stop(self):
        for block in self.blocks:
            block.speed = 0

    def shift(self,direction):
        for block in self.blocks:
            block.shift(direction)



class Block(pg.sprite.Sprite):
    image = None
    rect = None
    speed = 1
    position = [0.0,0.0]
    def __init__(self,x=0,y=0):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([24,24])
        self.image.fill(Colors.BLUE)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def update(self):
        self.position[0] += 0.05*self.speed
        self.rect.y = int(self.position[0])

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def shift(self,direction):
        self.rect.x += direction*25
