import pygame as pg 

# Inicialização do Pygame
pg.init()
screen = pg.display.set_mode((640,480))

# Definição das cores para caixa inativa e ativa
colorInactive = pg.Color(255,0,0)
colorActive = pg.Color(0,255,0)
FONT = pg.font.Font(None, 32)
values = []    


# Definição da classe (objeto) Inputbox
class Inputbox:

    # Função de inicialização da classe
    def __init__(self,x,y,w,h,txt=''):
        self.rect = pg.Rect(x,y,w,h)
        self.color = colorInactive
        self.txt = txt
        self.txt_surface = FONT.render(txt, True, self.color)
        self.active = False
        self.value = 0
    
    # Função de checagem de eventos
    def handle_event(self, event):
        # Checando se houve um clique dentro do retângulo
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
                    self.txt = ''
                elif event.key == pg.K_BACKSPACE:
                    self.txt = self.txt[:-1]
                else:
                    self.txt += event.unicode
                
                # Renderizar o texto novamente
                self.txt_surface = FONT.render(self.txt, True, self.color)

    def update(self):
        # Atualizando a largura do retângulo para o texto
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    
    def draw(self, screen):
        # Atualizando texto na tela
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Atualizando inputbox na tela
        pg.draw.rect(screen, self.color, self.rect, 2)
    
def main():
    FNN = Inputbox(100,100,140,32)
    FRP = Inputbox(100,150,140,32)
    input_boxes = [FNN, FRP]
    exportValues = [0]*len(input_boxes)
    done = False

    while not done: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
        
        for box in input_boxes:
            box.update()

        screen.fill((180,180,180))
        for box in input_boxes:
            box.draw(screen)    
        
        pg.display.flip()
        
        for i in range(len(input_boxes)):
            exportValues[i] = input_boxes[i].value
    
    return(exportValues)
            
        
if __name__ == '__main__':
    value = main()
    print(value)
    pg.quit()