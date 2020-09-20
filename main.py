# IMPORTAÇÃO DOS OBJETOS CRIADOS

from screenManager import Screen, Button, colours
from simOBJ import Inputbox
from screen_sim import Bolinha, Timer
import pygame as pg 
import numpy as np

# VARIÁVEIS GLOBAIS
# Aqui o Pygame é iniciado e são definidas todas as variáveis utilizadas como:
# altura e largura da janela, telas (menu de parâmetros, simulação e exibição dos resultados),
# input boxes para que o usuário possa inserir valores, botões, timer, etc.

pg.init()
pg.font.init()
w_w = 1024
w_h = 768
done = False
paramScreen = Screen("Valores", w_w, w_h) 
simScreen = Screen("Simulação", w_w, w_h)
win = paramScreen.makeCurrent()

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
exportValues = np.zeros(len(input_boxes)) # Lista com os valores de cada parâmetros para sem exportado
#buttonStart = Botao("Start", input_boxes, 775,655,80,32)
bStart = Button(775,665,80,32,(255,0,0),(0,255,0),None,20,(0,0,0),"Start")
bReturn = Button(775,665,80,32,(255,0,0),(0,255,0),None,20,(0,0,0),"Return")
#startbuttonStart = buttonStart(775,655,80,32,colours['black'], colours['red'], "Helvetica", 20, colours['white'], "Start")
valores = {}

# LOOP PRINCIPAL DA APLICAÇÃO
# Aqui todas as lógicas são definidas. Também é aplicado o sistema de gerenciamento de janelas para que
# o usuário possa interagir com todo o sistema.

while not done:
    mouse_pos = pg.mouse.get_pos()
    mouse_click = pg.mouse.get_pressed()
    paramScreen.screenUpdate()
    simScreen.screenUpdate()
    # INICIO DA TELA DE VARIAVEIS
    
    # Tela do menu de variáveis
    if paramScreen.checkUpdate():
        for event in pg.event.get():
            #buttonStart.handle_event(event)
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()
        #buttonStart.draw(paramScreen.screen)
        bStart.showButton(paramScreen.screen)

        for box in input_boxes:
            box.draw(paramScreen.screen)
        #valores = buttonStart.dic
        if bStart.focusCheck(mouse_pos,mouse_click):
            for box in input_boxes:
                valores[box.name] = box.value
        #if buttonStart.change:
            win = simScreen.makeCurrent()
            paramScreen.endCurrent()
            #print("muda de tela")
    # FIM DA TELA DE VARIAVEIS

    # INÍCIO DA TELA DE SIMULAÇÃO
    elif simScreen.checkUpdate():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        bReturn.showButton(simScreen.screen)
        if bReturn.focusCheck(mouse_pos, mouse_click):
            win = paramScreen.makeCurrent()
            simScreen.endCurrent()
        #print("to na segunda tela champz")
        print(valores)
    



    '''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True'''
    pg.display.update()
pg.quit()