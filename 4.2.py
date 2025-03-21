# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 15:38:10 2025

@author: ahbpl
"""

from Graphics import *

def main_402():
    wind = GraphWin("Face", 600, 600)
    wind.setCoords(0, 0, 100, 100)
    
    
    #Prompt the User for 2 mouse clicks
    message = Text(Point(50, 90), "Aqui está a minha cara ;)")
    message.draw(wind)
    
    #Draw face
    head = Circle(Point(50,45),30)
    head.draw(wind)
    
    l_eye = Oval(Point(30,48),Point(48,58))
    l_eye.draw(wind)
    
    r_eye = Circle(Point(60,55),8)
    r_eye.draw(wind)
    
    nose = Line(Point(50,43),Point(50,48))
    nose.draw(wind)
    
    mouth = Rectangle(Point(28,40),Point(72,36))
    mouth.draw(wind)


    wind.getMouse()
    wind.close()
    
main_402()