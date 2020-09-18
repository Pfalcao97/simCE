import pygame as pg 

pg.init()
w_w = 1024
w_h = 768
screen = pg.display.set_mode((w_w,w_h))
FONT = pg.font.Font(None, 32)
image = pg.image.load('imgbase.PNG')
#image = pg.transform.scale(image, (100,100))                   
white = (255, 255, 255) 
def main():
    done = False
    
    while not done:
        screen.fill(white)
        screen.blit(image, (0, 0))
        
        mousepos = pg.mouse.get_pos()
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
        pg.display.flip()
        print(mousepos[1],mousepos[0])
if __name__ == "__main__":
    main()
    pg.quit()