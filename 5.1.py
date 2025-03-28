# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 16:37:46 2025

@author: ahbpl
"""

from Graphics import *

def main_501():
    wind = GraphWin("Circle",500,520)
    wind.setCoords(0,0,50,52)
    
    message = Text(Point(5,105),"Click to start.")
    message.draw(wind)
    
    start = wind.getMouse()
    x = start.getX()
    y = start.getY()
    
    circle = Circle(Point(x,y),2) 
    circle.draw(wind)
    
    t=0
    gravt = []
    ant_gravt = []
    py_t = y
    py_r = 0
    
    while py_t > 1:
        
        py_r = y+sum(gravt)
        gravt += [round(py_t-py_r)]
        ant_gravt += [-round(py_t-py_r)]
        
        t += 1
        py_t = (-0.5)*(t)**2+y
        
        
    ground = round(py_r+gravt[-1]-1)
    gravt += [-ground,ground]+ant_gravt[::-1]+[0]
    cicl = len(gravt)
    
    for n in range(500):
        
        m = n%cicl

        circle.move((-1)**((n+x)//46),gravt[m])
        

        update(30)
    
    wind.close()
    
main_501()
    