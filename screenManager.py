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

class Button:
    def __init__(self, x, y, sizex, sizey, buttoncolour, fbuttoncolour, font, fontsize, fcolour, text):
    # posição x, posição y, tamanho em x, tamanho em y, cor do botão, cor do botão quando clicado, fonte,
    # tamanho da fonte, cor da fonte, texto

        self.x = x    
        self.y = y    
        self.sizex = sizex
        self.sizey = sizey
        self.buttoncolour = buttoncolour
        self.fbuttoncolour = fbuttoncolour
        self.fontsize = fontsize
        self.fcolour = fcolour
        self.text = text
        self.current = False
        self.buttonf = pg.font.SysFont(font, fontsize)

    def showButton(self, display):
        if self.current:
            pg.draw.rect(display, self.fbuttoncolour, (self.x, self.y, self.sizex, self.sizey))
        else:
            pg.draw.rect(display, self.buttoncolour, (self.x, self.y, self.sizex, self.sizey))

        textsurface = self.buttonf.render(self.text, True, self.fcolour)
        display.blit(textsurface, ((int(self.x + (self.sizex/2) - (self.fontsize/2)*(len(self.text)/2)) - 5, int((self.y + (self.sizey/2) - (self.fontsize/2)-4)))))
        
    def focusCheck(self, mousepos, mouseclick):
        if (mousepos[0] >= self.x and mousepos[0] <=  self.x + self.sizex and mousepos[1] >= self.y and mousepos[1] <= self.y + self.sizey):
            self.current = True
            return mouseclick[0]
        else:
            self.current = False
            return False

pg.init()
pg.font.init()

menuScreen = Screen("menu screen")
screen2 = Screen("screen 2")

win = menuScreen.makeCurrent()

done = False

testButton = Button(0, 0, 150, 50, colours['black'], colours['red'], "Helvetica", 20, colours['white'], "Test")
returnButton = Button(0, 0, 150, 50 , colours['white'], colours['blue'], "Arial", 20, colours['black'], "Return")

toggle = False

while not done:
    menuScreen.screenUpdate()
    screen2.screenUpdate()
    mouse_pos = pg.mouse.get_pos()
    mouse_click = pg.mouse.get_pressed()
    keys = pg.key.get_pressed()

    # código do menu screen
    if menuScreen.checkUpdate():
        screen2button = testButton.focusCheck(mouse_pos, mouse_click)
        testButton.showButton(menuScreen.returnTitle())

        if screen2button:
            win = screen2.makeCurrent()
            menuScreen.endCurrent()
        
    # código da segunda screen
    elif screen2.checkUpdate():
        returnb = returnButton.focusCheck(mouse_pos, mouse_click)
        returnButton.showButton(screen2.returnTitle())

        if returnb:
            win = menuScreen.makeCurrent()
            screen2.endCurrent()
        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    
    pg.display.update()
pg.quit()


