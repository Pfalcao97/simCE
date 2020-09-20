import pygame as pg 
import pygame.gfxdraw

pg.init()
w_w = 1024
w_h = 768
screen = pg.display.set_mode((w_w,w_h))
FONT = pg.font.Font(None, 20)
image = pg.image.load('imgbase.PNG')
#image = pg.transform.scale(image, (75,100))                   
a = "auhsuhsa"

white = (255, 255, 255)
black = (0,0,0) 
shadow = (90,90,90)
dic = {'FNN': 10.0, 'FRP': 1.0, 'SCD': -0.5, 'SCE': 0.0, 'SHI': 0.0, 'ERR': 1.0, 'ENR': 0.0, 'EPE': 0.005, 'PNS': 0.0, 'PRS': 0.0, 'PEX': 0.0, 'PRM': 0.0, 'PMN': 0.0, 'PLG': 0.0, 'SPP': 0.0, 'CSU': 0.0}

class bolinha:
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

fnn = bolinha('FNN',screen,450,130)
frp = bolinha('FRP',screen,560,130)
pex = bolinha('PEX',screen,250,350)
prm = bolinha('PRM',screen,380,350)
pmn = bolinha('PMN',screen,510,350)
plg = bolinha('PLG',screen,630,350)
csu = bolinha('CSU',screen,760,350)
scd = bolinha('SCD',screen,910,300)
sce = bolinha('SCE',screen,910,400)
shi = bolinha('SHI',screen,910,500)
err = bolinha('ERR',screen,100,300)
enr = bolinha('ENR',screen,100,400)
epe = bolinha('EPE',screen,100,500)
pns = bolinha('PNS',screen,250,660)
prs = bolinha('PRS',screen,380,660)
spp = bolinha('SPP',screen,510,520)
def main():
    done = False
    
    while not done:
        screen.fill(white)
        #screen.blit(image, (0, 0))
        fnn.draw()
        frp.draw()
        pex.draw()
        prm.draw()
        pmn.draw()
        plg.draw()
        csu.draw()
        scd.draw()
        sce.draw()
        shi.draw()
        err.draw()
        enr.draw()
        epe.draw()
        pns.draw()
        prs.draw()
        spp.draw()
        mousepos = pg.mouse.get_pos()
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
        pg.display.flip()
        #print(mousepos[1],mousepos[0])
if __name__ == "__main__":
    main()
    pg.quit()