import pygame as pg 

colours = {"white": (255,255,255), "black": (0,0,0), "red": (255,0,0), "green": (0,255,0), "blue": (0,0,255)}

class Screen():
    def __init__(self, title, width=640, height=480, fill=colours['white']):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill
        self.current = False
    
    def makeCurrent(self):
        pg.display.set_caption(self.title)
        self.current = True
        self.screen = pg.display.set_mode((self.width, self.height))

    def endCurrent(self):
        self.current = False

    def checkUpdate(self):
        return self.current

    def screenUpdate(self):
        if self.current:
            self.screen.fill(self.fill)

    def returnTitle(self):
        return self.screen