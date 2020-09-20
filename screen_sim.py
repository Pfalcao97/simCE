import pygame as pg 
import pygame.gfxdraw

pg.init()
w_w = 1024
w_h = 768
screen = pg.display.set_mode((w_w,w_h))
FONT = pg.font.Font(None, 20)
image = pg.image.load('imgbase.PNG')
#image = pg.transform.scale(image, (75,100))                   
white = (255, 255, 255)
black = (0,0,0) 
shadow = (90,90,90)
bg = (220,220,220)
values = {'FNN': 1.0, 'FRP': 1.0, 'SCD': -0.5, 'SCE': 0.0, 'SHI': 0.0, 'ERR': 1.0, 'ENR': 0.0, 'EPE': 0.005, 'PNS': 0.0, 'PRS': 0.0, 'PEX': 0.0, 'PRM': 0.0, 'PMN': 0.0, 'PLG': 0.0, 'SPP': 0.0, 'CSU': 0.0}

class Bolinha:
    def __init__(self, name, values, x, y, minsize, maxsize):
        self.name = name
        self.x = x
        self.y = y
        self.value = values[self.name]
        self.screen = screen
        self.name_surface = FONT.render(self.name,True,black)
        self.size = 15+int(self.value*10)
        self.minsize = minsize
        self.maxsize = maxsize
    
    def draw(self, screen):
        pg.gfxdraw.filled_circle(self.screen,self.x+2, self.y+2,self.size,shadow)
        pg.gfxdraw.filled_circle(self.screen,self.x, self.y,self.size,white)
        pg.gfxdraw.aacircle(self.screen,self.x, self.y,self.size,black)
        screen.blit(self.name_surface, (self.x-int(FONT.size(self.name)[0]/2), self.y-int(FONT.size(self.name)[1]/2)))
    
    def update(self, values):
        self.size = 15+int(values[self.name]*10)
        if self.size > self.maxsize:
            self.size = self.maxsize
        elif self.size < self.minsize:
            self.size = self.minsize
        screen.blit(self.name_surface, (self.x-int(FONT.size(self.name)[0]/2), self.y-int(FONT.size(self.name)[1]/2)))


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

clock = pg.time.Clock()
fnn = Bolinha('FNN',values,450,130,15,100)
frp = Bolinha('FRP',values,560,130,15,100)
pex = Bolinha('PEX',values,250,350,15,100)
prm = Bolinha('PRM',values,380,350,15,100)
pmn = Bolinha('PMN',values,510,350,15,100)
plg = Bolinha('PLG',values,630,350,15,100)
csu = Bolinha('CSU',values,760,350,15,100)
scd = Bolinha('SCD',values,910,300,15,100)
sce = Bolinha('SCE',values,910,400,15,100)
shi = Bolinha('SHI',values,910,500,15,100)
err = Bolinha('ERR',values,100,300,15,100)
enr = Bolinha('ENR',values,100,400,15,100)
epe = Bolinha('EPE',values,100,500,15,100)
pns = Bolinha('PNS',values,250,660,15,100)
prs = Bolinha('PRS',values,380,660,15,100)
spp = Bolinha('SPP',values,510,520,15,100)

# fnn = Bolinha('FNN',450,130)
# frp = Bolinha('FRP',560,130)
# pex = Bolinha('PEX',250,350)
# prm = Bolinha('PRM',380,350)
# pmn = Bolinha('PMN',510,350)
# plg = Bolinha('PLG',630,350)
# csu = Bolinha('CSU',760,350)
# scd = Bolinha('SCD',910,300)
# sce = Bolinha('SCE',910,400)
# shi = Bolinha('SHI',910,500)
# err = Bolinha('ERR',100,300)
# enr = Bolinha('ENR',100,400)
# epe = Bolinha('EPE',100,500)
# pns = Bolinha('PNS',250,660)
# prs = Bolinha('PRS',380,660)
# spp = Bolinha('SPP',510,520)

timer = Timer(10,850,50)
pg.time.set_timer(pg.USEREVENT+1,1000)
timer_event = pg.USEREVENT+1
elements = [fnn,frp,pex,prm,pmn,plg,csu,scd,sce,shi,err,enr,epe,pns,prs,spp]
def main():
    done = False
    
    while not done:
        clock.tick(30)
        screen.fill(bg)
        timer.draw(screen)
        #screen.blit(image, (0, 0))
        for element in elements:
            element.draw(screen)
        #mousepos = pg.mouse.get_pos()
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == timer_event:
                     timer.time -= 1
                timer.update()
        pg.display.flip()
        #print(mousepos[1],mousepos[0])
if __name__ == "__main__":
    main()
    pg.quit()