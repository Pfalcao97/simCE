import pygame as pg
import numpy as np 

# Inicialização do Pygame
pg.init()
colorInactive = pg.Color(255,0,0)
colorActive = pg.Color(0,255,0)
FONT = pg.font.Font(None, 32)

# Definição da classe (objeto) Inputbox
class Inputbox:

    # Função de inicialização da classe
    def __init__(self,name,x,y,w,h,txt='0'):
        self.rect = pg.Rect(x,y,w,h)
        self.color = colorInactive
        self.txt = txt
        self.txt_surface = FONT.render(txt, True, self.color)
        self.active = False
        self.value = 0
        self.name = name
        self.name_surface = FONT.render(name, True, self.color)
        self.width = w
        self.availableKeys = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.'] # Lista com caracteres possíveis
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
                    self.active = False
                    #self.txt = ''
                if event.key == pg.K_BACKSPACE:
                    self.txt = self.txt[:-1]
                elif event.unicode in self.availableKeys: # Limitando os caracteres
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