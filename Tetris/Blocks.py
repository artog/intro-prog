__author__ = 'iadam'

import Colors
import pygame as pg

class BlockShape(object):

    blocks = []
    shape = [[1]]
    position = [0,0]
    def __init__(self,lane):
        b = Block(lane)
        self.blocks.append(b)

    def draw(self,screen):
        for block in self.blocks:
            block.draw(screen)

    def update(self):
        for block in self.blocks:
            block.update()

    def rotate(self):
        r = []
        for i in range(len(self.shape[0])):
            r.append([])
            for j in range(len(self.shape)):
                r[-1].append(self.shape[j][i])
        self.shape = r



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
