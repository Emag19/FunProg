# -*- coding: utf-8 -*-
"""
Created on Fri May  2 16:14:03 2025

@author: ahbpl
"""
from math import pi

class esfera:
    def __init__(self,radios):
        self.getRadius = radios
        self.surfaceArea = 4*pi*radios**2
        self.volume = (4/3)*(radios**3)*pi

c = esfera(4)
print(c.getRadius, c.surfaceArea, c.volume)