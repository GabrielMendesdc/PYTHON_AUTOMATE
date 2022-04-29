#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))


# In[ ]:


import pyautogui as pag
import time
import os
import re
import keyboard as kb
from pathlib import Path
import win32api,win32con


def wait(onde):  #espera achar o png na tela pra prosseguir com o código
    path = f'png_wait/{str(onde)}'+'.png'
    x = pag.locateCenterOnScreen(path,grayscale=True)
    while not x:
        x = pag.locateCenterOnScreen(path,grayscale=True)
    return x

def checaerro(nome='error', region = ''):
    if region:
        for i in range(5):
            erro = pag.locateCenterOnScreen(f'png_wait/{nome}.png',grayscale=True, region=region)
            if erro:
                return erro
        return 'ok'
    for i in range(5):
        erro = pag.locateCenterOnScreen(f'png_wait/{nome}.png',grayscale=True)
        if erro:
            return erro
    return 'ok'


def checaedson():
    for i in range(5):
        edson = pag.locateOnScreen('png_wait/edson.png', region = (752, 465, 410, 148),grayscale=True)
        time.sleep(0.5)
        if edson:
            return True
    return False


def checagem(nf):
    for i in range(2):
        errocad2 = pag.locateCenterOnScreen('png_wait/nfe2.png',grayscale=True, region = (611, 323, 187, 600))
        errocad1 = pag.locateCenterOnScreen('png_wait/nfe1.png',grayscale=True, region = (611, 323, 187, 600))
        despesa1 = pag.locateCenterOnScreen('png_wait/999.png',grayscale=True, region = (611, 323, 187, 600))
        despesa2 = pag.locateCenterOnScreen('png_wait/99.png',grayscale=True, region = (611, 323, 187, 600))
    if despesa1 or despesa2:
        movepasta('despesa', nf)
        return 1
    if errocad1 or errocad2:
        movepasta('cadastro', nf)
        return 1


def checa_ceasa():
    pag.click(1028,223)
    for i in range(4):
        time.sleep(1)
        ceasa = checaerro(nome='ceasa',region = (1255, 838, 75, 42))
    pag.click(1388,236)  
    if ceasa != 'ok':
        return '99'
    else:
        return '51'
    
    
def checagem_seta(nf):
    for i in range(3):
        seta = pag.locateCenterOnScreen('png_wait/seta.png',grayscale=True,region=(423, 801, 121, 43))
        if seta:
            pag.click(960,540)
            for i in range(4):
                page()
                for i in range(2):
                    c = checagem(nf)
                    if c:
                        return 1
            return 0
    for i in range(2):
        c = checagem(nf)
        if c:
            return 1

                    
def checajafoi(nf):
    for i in range(3):
        jafoi = pag.locateCenterOnScreen('png_wait/jafoi.png',grayscale=True,region=(667, 496, 414, 75))
        tribu = pag.locateCenterOnScreen('png_wait/tribu.png',grayscale=True,region=(629, 476, 536, 76))
    if jafoi:
        movepasta('perfeito', nf)
        pag.press('enter')
        pag.click(539,319)  #NF-e
        pag.click(474,223)  #livro
        time.sleep(3)
        return 'ja'
    while tribu:
        pag.press('enter')
        tribu = pag.locateCenterOnScreen('png_wait/tribu.png',grayscale=True,region=(629, 476, 536, 76))

    
def loga(pastanf):
    wait("compras")
    pag.write(f"{user}")
    pag.press("enter")
    pag.write(f"{passw}")
    pag.press("enter")
    time.sleep(12)
    pag.click(235,33)  #conferencias
    pag.click(260,144)  #xml/nfe
    pag.click(960,264)  #ativa XML
    pag.click(539,319)  #NF-e
    pag.click(474,223)  #livro
    time.sleep(4)
    conta_voltas = False
    for nf in notas(pastanf):
        if conta_voltas:
            time.sleep(2)
            pag.click(539,319)  #NF-e
            pag.click(474,223)  #livro
        conta_voltas = True
        string = pastanf / nf
        print(string)
        kb.write(str(string))
        pag.press("enter")
        time.sleep(2)
        if checaerro('fornecedor', region=(796, 464, 328, 151)) != 'ok'        or checaerro('falha'     , region=(479, 434, 954, 154)) != 'ok':
            movepasta('despesa', nf)
            pag.press('enter')
            pag.click(539,319)  #NF-e
            pag.click(474,223)  #livro
            time.sleep(3)
            continue
        if checajafoi(nf) == 'ja':
            continue
        lança(nf)

        
def notas(pastanf):  
    for diretorio, subpastas, arquivos in os.walk(pastanf):
        for arquivo in arquivos:
            yield arquivo

    
def lança(nf):
    global financeiro
    pag.click(603,320)  #aba recepcao
    pag.click(580,225)  #editar
    pag.click(1063,458,clicks=3)  #nome
    time.sleep(0.5)
    kb.write('bot Gabriel')
    pag.click(644,222)
    time.sleep(0.5)
    pag.click(669,318)  #clica compras
    if checagem_seta(nf):
        return 1
    financeiro = checa_ceasa()
    pag.click(784,319)  #conferencia
    pag.click(550,222)  #joia
    pag.click(716,319)  #fiscal
    pag.click(550,222)  #joia
    pag.click(667,322)  #compras
    pag.click(550,222)  #joia
    pag.click(1110,225)  #pn
    erro = checaerro(region=(772, 488, 424, 59))
    if erro != 'ok':
        movepasta('cadastro', nf)
        pag.press('enter')
        pag.click(539,319)  #NF-e
        pag.click(474,223)  #livro
        time.sleep(3)
        return 0
    pag.press('enter')
    time.sleep(5)    
    orq = checaerro('orquidea',region=(928, 510, 211, 42))
    cfop = checaerro('cfop',region=(755, 467, 415, 80))
    if orq != 'ok' or cfop != 'ok':
        movepasta('cadastro', nf)
        pag.press('enter')
        alt('s')
        pag.click(539,319)  #NF-e
        pag.click(474,223)  #livro
        time.sleep(3)
        return 0
    if checajafoi(nf):
        return 1

    for i in range(4):
        time.sleep(1)
        pag.press('enter')
    if financeiro == '99':
        repete()
    pgto = checaerro('pgto',region=(781, 487, 401, 62))
    if pgto != 'ok':
        pag.press('enter')
        pag.press('enter')
        repete()
        return 0 
    if checaedson():
        for i in range(10):
            pag.press('enter')
        pag.click(564,198)
        kb.send('enter')
        kb.send('enter')
        movepasta('despesa', nf)
        return 0
    pag.click(595,201)
    time.sleep(1)
    alt('s')
    alt('s')
    time.sleep(3)
    alt('f4')
    time.sleep(1)
    alt('f4')
    for i in range(4):
        joia = pag.locateCenterOnScreen('png_wait/joia.png',region=(685, 203, 41, 45))
        if joia == 'ok':
            time.sleep(1)
            alt('f4')
    movepasta('perfeito', nf)

    
    
def movepasta(destino, nf):
    print(destino)
    if destino == 'cadastro':
        os.replace(f"N:/XML ENTRADA/LJ002/{mes_ano}/Cadastro OK/{nf}" ,
        f"N:/XML ENTRADA/LJ002/{mes_ano}/{nf}")
    if destino == 'despesa':
        os.replace(f"N:/XML ENTRADA/LJ002/{mes_ano}/Cadastro OK/{nf}" ,
        f"N:/XML ENTRADA/LJ002/{mes_ano}/Financeiro/{nf}")
    if destino == 'perfeito':
        os.replace(f"N:/XML ENTRADA/LJ002/{mes_ano}/Cadastro OK/{nf}" ,
        f"N:/XML ENTRADA/LJ002/{mes_ano}/Cadastro OK/Entrada Ok/{nf}")

    
    
def isNum():
    return win32api.GetKeyState(win32con.VK_NUMLOCK)


def alt(bt=''):
    kb.send(f'alt+{bt}')

    

def repete():
    pag.click(689,329)
    pag.click(496,357)
    pag.mouseDown(button='left')
    pag.moveTo(480,357)
    pag.mouseUp(button='left')
    kb.write('99')
    pag.press('enter')
    time.sleep(0.3) 
    
    
def page(d = 'pagedown'):
    kb.send('page down')
#     pag.PAUSE = 0.4
#     if isNum() == 0:
#         pag.press(d)
#         pag.press('numlock')
#     else:        
#         pag.press('numlock')
#         pag.press(d)
#         pag.press('numlock')
#     pag.PAUSE = 0.85


mes_ano = input("Digite o mes e o ano, exemplo: 2022-02 ")
user = input("Digite seu usuário jacsys ")
passw = input("Digite sua senha ")
pastanf = Path(f"N:/XML ENTRADA/LJ002/{mes_ano}/Cadastro OK")
pag.PAUSE = 1.1
financeiro = '51'

pag.hotkey('ctrl','shift','capslock')
loga(pastanf)
    


# In[2]:


# import pyautogui as pag
# import time
# pag.hotkey('ctrl','shift','capslock')
# time.sleep(3)
# print(pag.position())
# pag.hotkey('ctrl','shift','capslock')


# In[7]:


# x = (685,203)
# y = (726,248)
# d = y[0]-x[0],y[1]-x[1]
# print(f'{x[0],x[1],d[0],d[1]}')
    


# In[ ]:


# cancelar pag.click(564,198)
# editar pag.click(537,199)
# gravar pag.click(593,200)

