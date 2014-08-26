__author__ = 'iadam'

import pygame as pg
import Colors


class Game():
    screen = None

    lane = [126,151,176,201]

    def __init__(self,screen):
        self.screen = screen

    def update(self):
        self.drawEnviroment()

    def drawEnviroment(self):
        self.screen.fill(Colors.WHITE)
        pg.draw.line(self.screen,Colors.BLACK,(75, 0), (75, 650))

        # for i in range(9):
        #     pg.draw.line(self.screen,Colors.BLACK,(100+25*i,  0),(100+25*i,650))

        pg.draw.line(self.screen, Colors.BLACK, ( 325,  0), (325,650))
        pg.draw.line(self.screen, Colors.BLACK, (  75,650), (325,650))