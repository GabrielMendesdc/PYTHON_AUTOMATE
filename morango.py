#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *
from tkinter import ttk
from PIL.ImageTk import PhotoImage
from PIL import Image
import os
from datetime import date
import time

root = Tk()
root.config(bg = 'CadetBlue2')
root.title('XML CONTADOR')
root.iconbitmap("logo.ico")
w = Canvas(root, width=300, height=510, bg = 'CadetBlue2')

texts = ['CAD','XML','PEND']
xs = [85,175,260]
true = False

class Rectangle():
    def __init__(self, coords, color, texto):
        self.coords = coords
        x,y = self.coords[:2]
        self.color = color
        self.texto = texto
        self.tag = w.create_rectangle(*self.coords, fill=self.color)
        self.t = w.create_text(x+20,y+20, text = self.texto.get() ,font=('Helvetica 16 bold'))  
        
        
class Mes():
    def __init__(self, coords, color, texto):
        self.coords = coords
        x,y = self.coords[:2]
        self.color = color
        self.texto = texto
        self.rec = w.create_rectangle(*self.coords, fill=self.color)
        self.tex = w.create_text(x+20,y+20, text = self.texto.get() ,font=('Helvetica 16 bold')) 
    def bind(self,*args):
        w.tag_bind(self.rec,'<ButtonPress-1>',self.troca)
        w.tag_bind(self.tex,'<ButtonPress-1>',self.troca)
    def troca(self,*args):
        global mes,m,true
        if true:
            w.itemconfig(self.tex, text = lista[int(mes)-1])
            true = False
            cria(mes)
        else:
            w.itemconfig(self.tex, text = lista[int(mes)])
            true = True
            cria(f'0{int(mes)+1}')

            
for i in range(1,9):
    w.create_text(25, 60*i, text=f"Loja {i}", fill="black", font=('Helvetica 12 bold'))

for i in range(3):
    w.create_text(xs[i], 14, text=texts[i], fill="black", font=('Helvetica 16 bold'))
    
def search(pasta):
    for diretorio, subpastas, arquivos in os.walk(pasta):
        return len(arquivos)

    
def caminho(i,lj,mes):
    if i == 0 or i % 3 == 0:
        return fr'N:\XML ENTRADA\LJ00{lj}\2022-{mes}\\'
    if i == 1 or (i-1) % 3 == 0:
        return fr'N:\XML ENTRADA\LJ00{lj}\2022-{mes}\Cadastro OK\\'
    if i == 2 or (i-2) % 3 == 0:
        return fr'N:\XML ENTRADA\LJ00{lj}\2022-{mes}\Cadastro OK\Pendencia\\'

        
cords = [(60, 40, 110, 80),(147, 40, 197, 80),(234, 40, 284, 80),(60, 100, 110, 140),(147, 100, 197, 140),
        (234, 100, 284, 140),(60, 160, 110, 200),(147, 160, 197, 200),(234, 160, 284, 200),(60, 220, 110, 260),
        (147, 220, 197, 260),(234, 220, 284, 260),(60, 280, 110, 320),(147, 280, 197, 320),(234, 280, 284, 320),
        (60, 340, 110, 380),(147, 340, 197, 380),(234, 340, 284, 380),(60, 400, 110, 440),(147, 400, 197, 440),
        (234, 400, 284, 440),(60, 460, 110, 500),(147, 460, 197, 500),(234, 460, 284, 500)]    


def cria(mes):
    lj = 1
    for i in range(24):
        if i % 3 == 0 and i > 0:
            lj += 1
        s = StringVar(root, search(caminho(i,lj,mes)))
        color = 'light green'
        if search(caminho(i,lj,mes)) >= 40:
            color = 'red'
        elif search(caminho(i,lj,mes)) >= 25:
            color = 'orange'
        elif search(caminho(i,lj,mes)) >= 10:
            color = 'coral'
        elif search(caminho(i,lj,mes)) == 0:
            color = 'light grey'
        rect = Rectangle(cords[i],color,s)

mes = '01' 
m = StringVar()
lista = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']
m.set(lista[int(mes)-1])
bt = Mes((10,10,50,40),'white',m)
bt.bind()
cria(mes)
w.pack(expand=1)

mainloop()


# In[24]:


print(224+87,224+87+87,224+87+87+87)


# In[ ]:




