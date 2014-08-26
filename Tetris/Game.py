__author__ = 'Adam'

import pygame as pg
import Colors
from Blocks import BlockShape

class Game():
    screen = None

    blocks = []
    currentBlock = None
    lanes = (75,100,125,150,175,200,225,250,275,300)
    done = False

    def __init__(self,screen):
        self.screen = screen
        self.makeNewCurrent()

    def isDone(self):
        return self.done

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYUP:

                if event.key == pg.K_DOWN:
                    self.currentBlock.boost(False)

            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    self.done = True

                if event.key == pg.K_LEFT:
                    self.currentBlock.shift(-1)

                if event.key == pg.K_RIGHT:
                    self.currentBlock.shift(1)
                if event.key == pg.K_DOWN:
                    self.currentBlock.boost(True)


    def makeNewCurrent(self):
        print(self.currentBlock)
        b = None

        if isinstance(self.currentBlock,BlockShape):
            # currentTop = int(self.currentBlock.rect.top)
            # currentLane = int(self.currentBlock.lane)
            b = self.currentBlock.copy() #BlockShape(self.lanes,currentLane,currentTop)
            b.speed = 0

        self.currentBlock = BlockShape(self.lanes, 5, 0)
        if b != None:
            self.blocks.append(b)
        print(self.currentBlock)

    def update(self):
        self.drawEnviroment()

        self.currentBlock.update()

        if len(pg.sprite.spritecollide(self.currentBlock,self.blocks,False)) > 0 or self.currentBlock.rect.bottom >= 650:
            self.currentBlock.stop()
            self.makeNewCurrent()

        for block in self.blocks:
            block.draw(self.screen)

        self.currentBlock.draw(self.screen)


    def drawEnviroment(self):
        self.screen.fill(Colors.WHITE)
        pg.draw.line(self.screen,Colors.BLACK,(75, 0), (75, 650))

        # for i in range(9):
        #     pg.draw.line(self.screen,Colors.BLACK,(100+25*i,  0),(100+25*i,650))

        pg.draw.line(self.screen, Colors.BLACK, ( 325,  0), (325,650))
        pg.draw.line(self.screen, Colors.BLACK, (  75,650), (325,650))