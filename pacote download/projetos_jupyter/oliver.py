#!/usr/bin/env python
# coding: utf-8

# In[13]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))


# In[19]:


import pyautogui as pag
import time
import os
import re
import keyboard as kb
from pathlib import Path
import win32api,win32con

mes_ano = input("Digite o mes e o ano, exemplo: 2022-02 ")
user = input("Digite seu usuário jacsys ")
passw = input("Digite sua senha ")
pastanf = Path(f"N:/XML ENTRADA/LJ002/{mes_ano}/Cadastro OK")
pag.PAUSE = 1.1
financeiro = '51'


def wait(onde):  #espera achar o png na tela pra prosseguir com o código
    path = f'png_wait/{str(onde)}'+'.png'
    x = pag.locateCenterOnScreen(path)
    while not x:
        x = pag.locateCenterOnScreen(path)
    return x   


def checaerro(nome='error'):
    time.sleep(2)
    erro = pag.locateCenterOnScreen(f'png_wait/{nome}.png',grayscale=True)
    if erro:
        print(erro)
        return erro
    else:
        return 'ok'

    
def checajafoi(nf):
    jafoi = pag.locateCenterOnScreen('png_wait/jafoi.png',grayscale=True)
    if jafoi:
        print(jafoi)
        movepasta('perfeito', nf)
        pag.press('enter')
        pag.click(539,319)  #NF-e
        pag.click(474,223)  #livro
        time.sleep(3)
        return 'ja'
    tribu = pag.locateCenterOnScreen('png_wait/tribu.png',grayscale=True)
    while tribu:
        pag.press('enter')
        tribu = pag.locateCenterOnScreen('png_wait/tribu.png',grayscale=True)
        
    
def loga(pastanf):
    pag.click(1912,1064)
    pag.click(626,289, clicks = 2)
    wait("compras")
    pag.write(f"{user}")
    pag.press("enter")
    pag.write(f"{passw}")
    pag.press("enter")
    wait("conf")
    pag.click(235,33)  #conferencias
    pag.click(260,144)  #xml/nfe
    pag.click(960,264)  #ativa XML
    pag.click(539,319)  #NF-e
    pag.click(474,223)  #livro
    time.sleep(3)
    conta_voltas = False
    for nf in notas(pastanf):
        if conta_voltas:
            time.sleep(2)
            pag.click(539,319)  #NF-e
            pag.click(474,223)  #livro
        conta_voltas = True
        string = pastanf / nf
        print(string)
        time.sleep(0.5)
        kb.write(str(string))
        pag.press("enter")
        time.sleep(2)
        ja = checajafoi(nf)
        if ja == 'ja':
            continue
        lança(nf)

        
def notas(pastanf):  
    for diretorio, subpastas, arquivos in os.walk(pastanf):
        for arquivo in arquivos:
            yield arquivo
            

def cancelar():
    x = pag.locateCenterOnScreen('png_wait/cancelar.png',region = (582, 157, 37, 87))
    if not x:
        x = pag.locateCenterOnScreen('png_wait/cancelar.png',region = (582, 157, 37, 87))
    click(x)
    
    
def lança(nf):
    global financeiro
    pag.click(603,320)  #aba recepcao
    pag.click(1063,458,clicks=2)  #nome
    time.sleep(0.5)
    alt("e")
    kb.write('bot Gabriel')
    alt('g')
    time.sleep(0.5)
    pag.click(669,318)  #clica compras
    c = checagem_seta(nf)  
    if c:
        return 1
    pag.click(784,319)  #conferencia
    pag.click(550,222)  #joia
    pag.click(716,319)  #fiscal
    pag.click(550,222)  #joia
    pag.click(667,322)  #compras
    pag.click(550,222)  #joia
    pag.click(1110,225)  #pn
    time.sleep(3)
    erro = checaerro()
    ja = checajafoi(nf)
    if ja:
        return 1
    if erro != 'ok':
        print(checaerro())
        movepasta('cadastro', nf)
        pag.press('enter')
        pag.click(539,319)  #NF-e
        pag.click(474,223)  #livro
        time.sleep(3)
        return 0
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(5)
    pag.press('enter')
    time.sleep(0.5)
    pag.press('enter')
    if financeiro == '99':
        pag.click(689,329)
        pag.click(496,357)
        pag.mouseDown(button='left')
        pag.moveTo(480,357)
        pag.mouseUp(button='left')
        kb.write('99')
        pag.press('enter')
        time.sleep(0.3)
        alt('del')
        pag.press('enter')
    alt('g')
    if checaedson():
        for i in range(8):
            pag.press('enter')
        cancelar()
        kb.press('enter')
        kb.press('enter')
        movepasta('despesa', nf)
    alt('s')
    time.sleep(3)
    alt('f4')
    time.sleep(1)
    alt('f4')
    movepasta('perfeito', nf)
    
    

def checaedson():
    for i in range(7):
        edson = pag.locateOnScreen('png_wait/edson.png', region = (752, 465, 410, 148))
        time.sleep(0.5)
        if edson:
            pag.hotkey('ctrl','shift','capslock')
            return True
    return False
    
    
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
    

def checagem(nf):
    errocad2 = pag.locateCenterOnScreen('png_wait/nfe2.png',grayscale=True)
    errocad1 = pag.locateCenterOnScreen('png_wait/nfe1.png',grayscale=True)
    despesa1 = pag.locateCenterOnScreen('png_wait/999.png',grayscale=True)
    despesa2 = pag.locateCenterOnScreen('png_wait/99.png',grayscale=True)
    if despesa1 or despesa2:
        movepasta('despesa', nf)
        return 1
    if errocad1 or errocad2:
        movepasta('cadastro', nf)
        return 1

    
def checagem_seta(nf):
    global financeiro
    pag.click(1028,223)
    time.sleep(3)
    ceasa = checaerro(nome='ceasa')
    if ceasa != 'ok':
        financeiro = '99'
        print('99')
    else:
        financeiro = '51'
    pag.click(1388,236)      
    seta = pag.locateCenterOnScreen('png_wait/seta.png')
    if seta:
        pag.click(960,540)
        for i in range(4):
            page()
            c = checagem(nf)
            if c:
                return 1
            page()
            c = checagem(nf)
            if c:
                return 1
    c = checagem(nf)
    if c:
        return 1
    
    
def isNum():
    return win32api.GetKeyState(win32con.VK_NUMLOCK)


def alt(bt=''):
    pag.PAUSE = 0.3
    if isNum() == 0:
        pag.hotkey('alt',bt)
        pag.press('numlock')
    else:        
        pag.press('numlock')
        pag.hotkey('alt',bt)
        pag.press('numlock')
    pag.PAUSE = 0.85
    
    
def page(d = 'pagedown'):
    pag.PAUSE = 0.4
    if isNum() == 0:
        pag.press(d)
        pag.press('numlock')
    else:        
        pag.press('numlock')
        pag.press(d)
        pag.press('numlock')
    pag.PAUSE = 0.85
    
    
pag.hotkey('ctrl','shift','capslock')
loga(pastanf)


# In[16]:



pag.hotkey('ctrl','shift','capslock')
time.sleep(2)
print(pag.position())
pag.hotkey('ctrl','shift','capslock')


# In[18]:


x = (582,157)
y = (619,244)
d = y[0]-x[0],y[1]-x[1]
print(x, d)


# In[ ]:




