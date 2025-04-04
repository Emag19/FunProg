# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 11:33:20 2025

@author: ahbpl
"""

#face.py
from Graphics import *

class Face:
    def __init__(self, window, center, size):
        self.size = size
        self.eyeSize = 0.15 * size
        self.eyeOff = size / 3.0
        self.mouthSize = 0.8 * size
        self.mouthOff = size / 2.0
        self.center = center
        self.window = window
        self.initializeGrimFace()
        self.rightEye
        
    def getCenter(self):
        return self.center
    
    def move(self, dx, dy):
        self.unDraw()
        center = self.getCenter()
        x = center.getX()
        y = center.getY()
        self.center = Point(x + dx, y + dy)
#        if dx < 0 and dy < 0:
 #           self.smile()
  #      elif dx < 0 and dy > 1:
   #         self.wink()
    #    elif dx > 0 and dy > 0:
        self.initializeGrimFace()
      #  else:
        #self.meditate()
        
    def initializeGrimFace(self):
        self.head = Circle(self.center, self.size)
        self.leftEyeOpen()
        self.rightEyeOpen()
        self.teeth = []
        self.lineMouth()
        self.drawFace()
        
    def lineMouth(self):
        p1 = self.center.clone()
        p1.move(-self.mouthSize/2, self.mouthOff)
        p2 = self.center.clone()
        p2.move(self.mouthSize/2, self.mouthOff)
        self.mouth = Line(p1, p2)
        return Line(p1, p2)
    
    def rectMouth(self):
        p1, p2 = self.mouth.getP1(), self.mouth.getP2()
        x1, x2, y1, y2 = p1.getX(), p2.getX(), p1.getY(), p2.getY()
        offset = self.eyeSize / 2
        self.mouth = Rectangle(Point(x1, y1 - offset), Point(x2, y2 + offset))
        return x2, x1, y1, y2, offset
    
    def unDraw(self):
        self.head.undraw()
        self.leftEye.undraw()
        self.rightEye.undraw()
        self.mouth.undraw()
        for tooth in self.teeth:
            tooth.undraw()
        
    def drawFace(self):
        self.head = Circle(self.center, self.size)
        self.head.draw(self.window)
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        self.mouth.draw(self.window)
        
    def leftEyeOpen(self):
        self.leftEye = Circle(self.center, self.eyeSize)
        self.leftEye.move(-self.eyeOff, -self.eyeOff)
        
    def rightEyeOpen(self):
        self.rightEye = Circle(self.center, self.eyeSize)
        self.rightEye.move(self.eyeOff, -self.eyeOff)
        
    def leftEyeWink(self):
        center = self.leftEye.getCenter()
        x = center.getX()
        y = center.getY()
        leftWink = Line(Point(x - self.eyeSize, y), Point(x + self.eyeSize, y))
        self.leftEye = leftWink
        
    def rightEyeWink(self):
        center = self.rightEye.getCenter()
        x = center.getX()
        y = center.getY()
        rightWink = Line(Point(x - self.eyeSize, y), Point(x + self.eyeSize, y))
        self.rightEye = rightWink
        
    def wink(self):
        self.unDraw()
        self.lineMouth()
        self.leftEyeOpen()
        self.rightEyeWink()
        self.drawFace()
        
    def smile(self):
        self.unDraw()
        x2, x1, y1, y2, offset = self.rectMouth()
        xint = abs(x2 - x1) / 8
        self.teeth.append(self.lineMouth())
        for i in range (8):
            t2 = Line(Point(x1 + i * xint, y1 - offset), Point((x1 + i * xint), y2 + offset))
            self.teeth.append(t2)
        for tooth in self.teeth:
            tooth.draw(self.window)
            self.rectMouth()
            self.leftEyeOpen()
            self.rightEyeOpen()
            self.drawFace()
        
    def meditate(self):
        self.unDraw()
        self.lineMouth()
        self.leftEyeWink()
        self.rightEyeWink()
        self.drawFace()
        
        
    def movement(self,coords,total=200,rate=10):
        
        size = abs(self.size)*2
        start = self.center   
        y = start.getY()-size/2
        x = start.getX()-size/2
        #coords - (x1,y1,x2,y2)
        width = coords[2]-coords[0]
        height = coords[3]-coords[1]

        for n in range(total):
            self.move((-1)**((n+x)//(width-size)),(-1)**((n+y)//(height-size)))

            update(rate)
            
        
 
win = GraphWin("Cara móvel",600,600)
win.setCoords(0, 0, 60, 60)


f = Face(win,Point(30,30),-5)
f.movement((0, 0, 60, 60))
win.getMouse()
win.close()