#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui as pag
import keyboard as kb
import time

foi = False
deu = False
pag.PAUSE = 1
while True:
    if kb.is_pressed('enter'):
        foi = True
        if foi:
            time.sleep(3)
            pag.click(703,365)
            foi = False
    if kb.is_pressed('space'):
        deu = True
        if deu:
            pag.click(729,228)
            kb.press('enter')
            time.sleep(0.5)
            kb.send('alt+l')
            time.sleep(0.5)
            kb.write('/nf')
            deu = False
    if kb.is_pressed('='):
        sim = True
        if sim:
            kb.send('alt+e')
            time.sleep(2)
            pag.click(693,360)
            time.sleep(1.5)
            kb.write('99')
            kb.send('alt+g')
            time.sleep(2)
            kb.send('alt+l')
            time.sleep(0.5)
            kb.write('/nf')
            kb.send('alt+f4')
            time.sleep(0.5)
            kb.send('alt+l')
            time.sleep(0.5)
            kb.write('/nf')
            sim = False


# In[ ]:




