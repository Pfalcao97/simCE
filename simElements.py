import pygame as pg 
import pygame.gfxdraw

# Inicialização do Pygame
pg.init()
w_w = 1024
w_h = 768
screen = pg.display.set_mode((w_w,w_h))
FONT = pg.font.Font(None, 20)
white = (255, 255, 255)
black = (0,0,0) 
shadow = (90,90,90)
bg = (220,220,220)

# Definição do objeto bolinha
class Bolinha:

    # Função de inicialização da classe
    def __init__(self, name, values, x, y, minsize, maxsize):
        self.name = name
        self.x = x
        self.y = y
        self.value = values[self.name]
        self.screen = screen
        self.name_surface = FONT.render(self.name,True,black)
        self.size = 30
        self.minsize = minsize
        self.maxsize = maxsize
    
    def draw(self, screen):
        pg.gfxdraw.filled_circle(self.screen,self.x+2, self.y+2,self.size,shadow)
        pg.gfxdraw.filled_circle(self.screen,self.x, self.y,self.size,white)
        pg.gfxdraw.aacircle(self.screen,self.x, self.y,self.size,black)
        screen.blit(self.name_surface, (self.x-int(FONT.size(self.name)[0]/2), self.y-int(FONT.size(self.name)[1]/2)))
    
    def update(self, values):
        self.size = int(values[self.name]*10)
        if self.size > self.maxsize:
            self.size = self.maxsize
        elif self.size < self.minsize:
            self.size = self.minsize
        screen.blit(self.name_surface, (self.x-int(FONT.size(self.name)[0]/2), self.y-int(FONT.size(self.name)[1]/2)))

# Definição do objeto Timer
class Timer:
    def __init__(self, time, x, y):
        self.screen = screen
        self.time = time
        self.x = x
        self.y = y
        self.counter_surface = FONT.render(str(self.time), True, black)
        self.timer_txt = FONT.render("Timer: ", True, black)
        
    def update(self):
        # if event.type == self.timer_event:
        #     self.time -= 1
        self.counter_surface = FONT.render(str(self.time), True, black)
    
    def draw(self, screen):
        screen.blit(self.counter_surface, (self.x,self.y))
        screen.blit(self.timer_txt, (self.x-60,self.y))