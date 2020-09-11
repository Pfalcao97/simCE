import pygame as pg
import numpy as np 

# Inicialização do Pygame
pg.init()
w_w = 1024
w_h = 768
screen = pg.display.set_mode((w_w,w_h))

# Definição das cores para caixa inativa e ativa
colorInactive = pg.Color(255,0,0)
colorActive = pg.Color(0,255,0)
FONT = pg.font.Font(None, 32)
values = [] 


# Definição da classe (objeto) Inputbox
class Inputbox:

    # Função de inicialização da classe
    def __init__(self,name,x,y,w,h,txt=''):
        self.rect = pg.Rect(x,y,w,h)
        self.color = colorInactive
        self.txt = txt
        self.txt_surface = FONT.render(txt, True, self.color)
        self.active = False
        self.value = 0
        self.name = name
        self.name_surface = FONT.render(name, True, self.color)
        self.width = w
    
    # Função de checagem de eventos
    def handle_event(self, event):
        # Checando se ha clique dentro do retângulo
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        # Mudando a cor da caixa
        self.color = colorActive if self.active else colorInactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    print(self.txt)
                    self.value = float(self.txt)
                    #self.txt = ''
                elif event.key == pg.K_BACKSPACE:
                    self.txt = self.txt[:-1]
                else:
                    self.txt += event.unicode
                
                # Renderizar o texto novamente
                self.txt_surface = FONT.render(self.txt, True, self.color)

     
        

    def update(self):
        # Atualizando a largura do retângulo para o texto
        width = max(self.width, self.txt_surface.get_width()+10)
        self.rect.w = width
    
    def draw(self, screen):
        # Atualizando texto na tela
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Atualizando inputbox na tela
        pg.draw.rect(screen, self.color, self.rect, 2)
        # Desenhando nome do parâmetro na tela
        screen.blit(self.name_surface, (self.rect.x+250, self.rect.y+5))

# Definição da classe (objeto) botão        
class botao:

    # Função de inicialização da classe
    def __init__(self,name,input_boxes,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.b = pg.Rect(x,y,w,h) # função 4-dimensões
        self.name = name
        self.color = pg.Color(0,0,0)
        self.name_surface = FONT.render(name, True, self.color)
        #self.exportValues = exportValues
        self.input_boxes = input_boxes
        self.dic = {}
        

    # Desenhando o botão na tela
    def draw(self, screen):
        pg.draw.rect(screen,(255,0,0),self.b)
        screen.blit(self.name_surface, (self.b.x+15, self.b.y+5))

    def handle_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.b.collidepoint(event.pos):
                for box in self.input_boxes:
                    self.dic[box.name] = box.value
                        #print(self.exportValues)
                print(self.dic)


def main():

    # Definição de parâmetros
    FNN = Inputbox("FNN",100,100,50,32)
    FRP = Inputbox("FRP",100,150,50,32)
    SCD = Inputbox("SCD",100,200,50,32)
    SCE = Inputbox("SCE",100,250,50,32)
    SHI = Inputbox("SHI",100,300,50,32)
    ERR = Inputbox("ERR",100,350,50,32)
    ENR = Inputbox("ENR",100,400,50,32)
    EPE = Inputbox("EPE",100,450,50,32)
    PNS = Inputbox("PNS",600,100,50,32)
    PRS = Inputbox("PRS",600,150,50,32)
    PEX = Inputbox("PEX",600,200,50,32)
    PRM = Inputbox("PRM",600,250,50,32)
    PMN = Inputbox("PMN",600,300,50,32)
    PLG = Inputbox("PLG",600,350,50,32)
    SPP = Inputbox("SPP",600,400,50,32)
    CSU = Inputbox("CSU",600,450,50,32)
    # Armazenamento dos parâmetros numa lista
    input_boxes = [FNN, FRP, SCD, SCE, SHI, ERR, ENR, EPE, PNS, PRS, PEX, PRM, PMN, PLG, SPP, CSU]
    #exportValues = [0]*len(input_boxes) # Lista com os valores de cada parâmetros para sem exportado
    exportValues = np.zeros(len(input_boxes)) # Lista com os valores de cada parâmetros para sem exportado
    button = botao("start", input_boxes, 775,655,80,32)
    done = False
    

    # Loop principal
    while not done:
        # Checando os possíveis eventos
        for event in pg.event.get():
            button.handle_event(event)
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
        
        # Loop para atualizar as inputs
        for box in input_boxes:
            box.update()

        # Desenhando tela
        screen.fill((180,180,180))
        button.draw(screen)
        for box in input_boxes:
            box.draw(screen)    
        pg.display.flip()
        
        # Exportando os valores inseridos
        for i in range(len(input_boxes)):
            exportValues[i] = input_boxes[i].value
    return(exportValues)


        
if __name__ == '__main__':
    value = main()
    pg.quit()