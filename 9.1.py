# -*- coding: utf-8 -*-
"""
Created on Mon May 12 10:23:08 2025

@author: ahbpl
"""

from graphics import *
from time import sleep

global lt_x, lt_y

lt_x = []
lt_y = []

def media(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma/len(lista)

def reta():
    m_x = media(lt_x)
    m_y = media(lt_y)
    n = len(lt_y)
    s_cima = 0
    s_baixo = 0
    
    for i in range(n):
        s_cima += lt_x[i]*lt_y[i] - n*m_y*m_x
    for x in lt_x:
        s_baixo += x**2 - n*(m_x**2)
    
    dc = s_cima/s_baixo
    print(s_cima,s_baixo,dc)

    return [(-100,m_y + dc*(-100-m_x)),
                (100,m_y + dc*(100-m_x))]


class Button:
    
    def __init__(self, janela, ct_inf_esq, ct_sup_dir, texto="Concluído"):
        x1,y1 = ct_inf_esq
        x2,y2 = ct_sup_dir
        self.pts = [x1,y1,x2,y2]
        self.janela = janela
        self.retangulo = Rectangle(Point(x1,y1), Point(x2,y2))
        self.retangulo.draw(janela)
        self.retangulo.setFill(color_rgb(182,197,184))
        self.texto = texto
  
    def click(self):
        self.retangulo.setFill(color_rgb(255,50,100))
        p1,p2 = reta()
        linha = Line(Point(p1[0],p1[1]),Point(p2[0],p2[1]))
        linha.draw(self.janela)
        sleep(2)
        self.retangulo.setFill(color_rgb(182,197,184))
        self.janela.getMouse()
        self.janela.close()

    def etiqueta(self):
        x1,y1,x2,y2 = self.pts
        etiqueta = Text(Point(x1+(x2-x1)/2,y1+(y2-y1)/2),self.texto)
        etiqueta.draw(self.janela)

win = GraphWin("Linha de tendencia.",600,600)
win.setCoords(-100,-100,100,100)

eixo_x = Line(Point(-100,0),Point(100,0))
eixo_y = Line(Point(0,-100),Point(0,100))
eixo_x.draw(win)
eixo_y.draw(win)



b = Button(win, (69,89), (99,99))
b.etiqueta()

while True:
    ponto = win.checkMouse()
    if ponto != None:
        x1,y1,x2,y2 = b.pts
        
        if (x1 <= ponto.getX() <= x2 and y1 <= ponto.getY() <= y2):
            b.click()
        else:
            lt_x += [ponto.getX()]
            lt_y += [ponto.getY()]
            ponto.draw(win)
    
    