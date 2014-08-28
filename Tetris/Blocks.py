__author__ = 'iadam'

import Colors
import pygame as pg

class BlockShape():
    def __init__(self,lanes,lane=0,y=0,shape=[[1,1]]):

        self.shapeBlocks = []
        self.shape = shape

        self.position = [lanes[lane],y]
        self.rect = pg.Rect(
            self.position[0],
            self.position[1],
            1,
            1
        )

        self.lanes = lanes
        self.lane = lane

        self.speed = 1

        self.makeBlocks()

        self.calcRect()

    def boost(self,active):
        if active:
            speed = 3
        else:
            speed = 1
        for block in self.shapeBlocks:
            block.speed = speed

    def makeBlocks(self):
        self.shapeBlocks = []
        for i in range(len(self.shape)):
            row = self.shape[i]
            for j in range(len(row)):
                b = Block(
                    self.lanes[self.lane+j],
                    self.rect.y+i*25,
                    self.lane+j,
                    self.lanes
                )
                self.shapeBlocks.append(b)

    def copy(self):
        b = BlockShape(self.lanes,self.lane,self.rect.y)
        return b

    def calcRect(self):
        top = 1000000
        left = 1000000
        bottom = 0
        right = 0
        for block in self.shapeBlocks:
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
        for block in self.shapeBlocks:
            block.draw(screen)

    def update(self):
        for block in self.shapeBlocks:
            block.update()
        self.calcRect()

    def rotate(self):
        r = []
        for i in range(len(self.shape[0])):
            r.append([])
            for j in range(len(self.shape)):
                r[-1].append(self.shape[j][i])
        self.shape = r
        self.makeBlocks()

    def stop(self):
        for block in self.shapeBlocks:
            block.speed = 0

    def shift(self,direction):
        self.lane += direction
        if len(self.lanes) <= self.lane:
            self.lane = len(self.lanes)-1
        if 0 > self.lane:
            self.lane = 0

        for block in self.shapeBlocks:
            block.shift(direction)



class Block(pg.sprite.Sprite):

    def __init__(self,x=0,y=0,lane=0,lanes=()):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface([25,25])
        self.image.fill(Colors.BLUE)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.lane = lane
        self.lanes = lanes

        self.speed = 1
        self.position = [x,y]

    def update(self):
        self.position[1] += 0.05*self.speed
        self.rect.y = int(self.position[1])

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def shift(self,direction):
        self.lane += direction
        if len(self.lanes) <= self.lane:
            self.lane = len(self.lanes)-1
        if 0 > self.lane:
            self.lane = 0

        self.rect.x = self.lanes[self.lane]
