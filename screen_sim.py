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
dic = {'FNN': 10.0, 'FRP': 1.0, 'SCD': -0.5, 'SCE': 0.0, 'SHI': 0.0, 'ERR': 1.0, 'ENR': 0.0, 'EPE': 0.005, 'PNS': 0.0, 'PRS': 0.0, 'PEX': 0.0, 'PRM': 0.0, 'PMN': 0.0, 'PLG': 0.0, 'SPP': 0.0, 'CSU': 0.0}

class Bolinha:
    def __init__(self, name, screen, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.screen = screen
        self.name_surface = FONT.render(self.name,True,black)

    def draw(self):
        size = 15+int(dic[self.name]*1)
        pg.gfxdraw.filled_circle(screen,self.x+2, self.y+2,size,shadow)
        pg.gfxdraw.filled_circle(screen,self.x, self.y,size,white)
        pg.gfxdraw.aacircle(screen,self.x, self.y,size,black)
        screen.blit(self.name_surface, (self.x-int(FONT.size(self.name)[0]/2), self.y-int(FONT.size(self.name)[1]/2)))

class Timer:
    def __init__(self, screen, time, x, y):
        self.screen = screen
        self.time = time
        self.x = x
        self.y = y
        self.counter_surface = FONT.render(str(self.time), True, black)
        self.timer_event = pg.USEREVENT+1
        self.timer_txt = FONT.render("Timer: ", True, black)
        
    def handle_event(self,event):
        if event.type == self.timer_event:
            self.time -= 1
            self.counter_surface = FONT.render(str(self.time), True, black)
    
    def draw(self, screen):
        screen.blit(self.counter_surface, (self.x,self.y))
        screen.blit(self.timer_txt, (self.x-60,self.y))

clock = pg.time.Clock()
fnn = Bolinha('FNN',screen,450,130)
frp = Bolinha('FRP',screen,560,130)
pex = Bolinha('PEX',screen,250,350)
prm = Bolinha('PRM',screen,380,350)
pmn = Bolinha('PMN',screen,510,350)
plg = Bolinha('PLG',screen,630,350)
csu = Bolinha('CSU',screen,760,350)
scd = Bolinha('SCD',screen,910,300)
sce = Bolinha('SCE',screen,910,400)
shi = Bolinha('SHI',screen,910,500)
err = Bolinha('ERR',screen,100,300)
enr = Bolinha('ENR',screen,100,400)
epe = Bolinha('EPE',screen,100,500)
pns = Bolinha('PNS',screen,250,660)
prs = Bolinha('PRS',screen,380,660)
spp = Bolinha('SPP',screen,510,520)

timer = Timer(screen,10,850,50)
pg.time.set_timer(pg.USEREVENT+1,1000)
elements = [fnn,frp,pex,prm,pmn,plg,csu,scd,sce,shi,err,enr,epe,pns,prs,spp]
def main():
    done = False
    
    while not done:
        clock.tick(30)
        screen.fill(bg)
        timer.draw(screen)
        #screen.blit(image, (0, 0))
        for element in elements:
            element.draw()
        #mousepos = pg.mouse.get_pos()
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                timer.handle_event(event)
        pg.display.flip()
        #print(mousepos[1],mousepos[0])
if __name__ == "__main__":
    main()
    pg.quit()