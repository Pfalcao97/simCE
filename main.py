# IMPORTAÇÃO DOS OBJETOS CRIADOS #

from screenManager import Screen, Button
from simOBJ import Inputbox
from screen_sim import Bolinha, Timer
import pygame as pg 
import numpy as np
import pandas as pd 
import operator

# VARIÁVEIS GLOBAIS #
# Aqui o Pygame é iniciado e são definidas todas as variáveis utilizadas como:
# altura e largura da janela, telas (menu de parâmetros, simulação e exibição dos resultados),
# input boxes para que o usuário possa inserir valores, botões, timer, etc.

pg.init()
pg.font.init()
w_w = 1024
w_h = 768
done = False
colours = {"white": (255,255,255), "black": (0,0,0), "shadow": (90,90,90), "bg": (220,220,220), "red": (255,0,0), "green": (0,255,0), "blue": (0,0,255)}
values = {'FNN': 0.0, 'FRP': 0.0, 'SCD': 0.0, 'SCE': 0.0, 'SHI': 0.0, 'ERR': 0.0, 'ENR': 0.0, 'EPE': 0.0, 'PNS': 0.0, 'PRS': 0.0, 'PEX': 0.0, 'PRM': 0.0, 'PMN': 0.0, 'PLG': 0.0, 'SPP': 0.0, 'CSU': 0.0}
# Janelas
paramScreen = Screen("Valores", w_w, w_h, fill=colours['bg']) 
simScreen = Screen("Simulação", w_w, w_h, fill=colours['bg'])
win = paramScreen.makeCurrent() # Tela atual

# Botões
bStart = Button(775,665,150,50,colours['blue'],colours['blue'],None,40,colours['black'],"Start")
bReturn = Button(775,665,150,50,colours['red'],colours['red'],None,40,colours['black'],"Return")
bResults = Button(775,665,80,32,colours['green'],colours['green'],None,40,colours['black'],"Results")

# REFERENTA À TELA DE PARÂMETROS #

# Parâmetros para tela de valores
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

# REFERENTE À TELA DE SIMULAÇÃO #
# Timer
clock = pg.time.Clock()
timer = Timer(10,850,50)
pg.time.set_timer(pg.USEREVENT+1,1000)
timer_event = pg.USEREVENT+1
minsize = 15
maxsize = 50
# Cálculos da simulação
op = {"+": operator.add, "-": operator.sub} # Operadores para os tipos de interações
tabela = pd.read_csv("interactions.csv", index_col=0) # Tabela de interações
factor = 0.5 # Fator multiplicativo
dim = len(tabela.index) # Tamanho da tabela
# Elementos
fnn = Bolinha('FNN',values,450,130,minsize, maxsize)
frp = Bolinha('FRP',values,560,130,minsize, maxsize)
pex = Bolinha('PEX',values,250,350,minsize, maxsize)
prm = Bolinha('PRM',values,380,350,minsize, maxsize)
pmn = Bolinha('PMN',values,510,350,minsize, maxsize)
plg = Bolinha('PLG',values,630,350,minsize, maxsize)
csu = Bolinha('CSU',values,760,350,minsize, maxsize)
scd = Bolinha('SCD',values,910,300,minsize, maxsize)
sce = Bolinha('SCE',values,910,400,minsize, maxsize)
shi = Bolinha('SHI',values,910,500,minsize, maxsize)
err = Bolinha('ERR',values,100,300,minsize, maxsize)
enr = Bolinha('ENR',values,100,400,minsize, maxsize)
epe = Bolinha('EPE',values,100,500,minsize, maxsize)
pns = Bolinha('PNS',values,250,660,minsize, maxsize)
prs = Bolinha('PRS',values,380,660,minsize, maxsize)
spp = Bolinha('SPP',values,510,520,minsize, maxsize)

# Armazenamento dos elementos numa lista
elements = [fnn,frp,pex,prm,pmn,plg,csu,scd,sce,shi,err,enr,epe,pns,prs,spp]


# Valores finais


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
                values[box.name] = box.value
        #if buttonStart.change:
            win = simScreen.makeCurrent()
            paramScreen.endCurrent()
            #print("muda de tela")
    # FIM DA TELA DE VARIAVEIS

    # INÍCIO DA TELA DE SIMULAÇÃO
    elif simScreen.checkUpdate():
        clock.tick(30)
        timer.draw(simScreen.screen)
        bReturn.showButton(simScreen.screen)
        for element in elements:
            element.draw(simScreen.screen)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == timer_event:
                timer.time -= 1
                # Loop para atualização dos valores dos parâmetros
                for i in range (dim):
                    for j in range (dim):
                        a = tabela.index[i]
                        b = tabela.index[j]
                        operation = tabela.loc[a,b]
                        if pd.isnull(operation):
                            pass
                        else:
                            values[a] = op[operation](values[a],factor*values[b])
                for element in elements:
                    element.update(values)
                if timer.time == 0:
                    print("cabo a graça")
                print(values)
                timer.update()

        
        
        
        
        
        if bReturn.focusCheck(mouse_pos, mouse_click):
            win = paramScreen.makeCurrent()
            simScreen.endCurrent()
        #print("to na segunda tela champz")
        
    



    '''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True'''
    pg.display.update()
pg.quit()