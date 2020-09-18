from screenManager import Screen, colours
from simOBJ import main, Inputbox, botao
import pygame as pg 
import numpy as np


pg.init()
pg.font.init()
done = False
valuesMenu = Screen("Valores",1024,768)
simScreen = Screen("Simulação", 1024,768 )
win = valuesMenu.makeCurrent()

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
#startButton = Button(775,655,80,32,colours['black'], colours['red'], "Helvetica", 20, colours['white'], "Start")
valores = {}

while not done:
    # INICIO DA TELA DE VARIAVEIS
    valuesMenu.screenUpdate()
    simScreen.screenUpdate()
    # Tela do menu de variáveis
    if valuesMenu.checkUpdate():
        for event in pg.event.get():
            button.handle_event(event)
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()
        button.draw(valuesMenu.screen)

        for box in input_boxes:
            box.draw(valuesMenu.screen)
        valores = button.dic
        if button.change:
            win = simScreen.makeCurrent()
            valuesMenu.endCurrent()
            #print("muda de tela")
    # FIM DA TELA DE VARIAVEIS

    # INÍCIO DA TELA DE SIMULAÇÃO
    elif simScreen.checkUpdate():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        print(valores)
    



    '''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True'''
    pg.display.update()
print(button.dic)
pg.quit()