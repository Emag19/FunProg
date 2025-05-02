#FunProg
from graphics import *
import math

class cubo:
    def __init__(self, aresta):
        self.getRadius = aresta
    
    def aresta(self):
        return self.getRadius
        
    def faceArea(self):
        return self.getRadius * self.getRadius
    
    def surfaceArea(self):
        return ((self.getRadius * self.getRadius) * 6)
    
    def volume (self):
        return (self.getRadius * self.getRadius * self.getRadius)
    
    def draw3I (self):
        
        win = GraphWin("Cubo 3I",500,500)
        win.setCoords(-200, -200, 200, 200)

        point1 = Point(0,0)
        point2 = Point(0,self.getRadius)
        x = float((math.sqrt(3)/2) * self.getRadius)
        y = float(0.5*self.getRadius)
        point3 = Point(x, y)
        point4 = Point(-x, y)
        point5 = Point(x, y + self.getRadius)
        point6 = Point(-x, y + self.getRadius)
        point7 = Point(0, 2 * self.getRadius)
        line1 = Line(point1, point4)
        line2 = Line(point4, point6)
        line3 = Line(point6, point7)
        lina4 = Line(point7, point5)
        line5 = Line(point5, point3)
        line6 = Line(point3, point1)
        line7 = Line(point1, point2)
        line8 = Line(point2, point6)
        line9 = Line(point2, point5)
        
        line1.draw(win)
        line2.draw(win)
        line3.draw(win) 
        lina4.draw(win) 
        line5.draw(win) 
        line6.draw(win) 
        line7.draw(win) 
        line8.draw(win) 
        line9.draw(win)
        
        win.getMouse()
        win.close()
        
    def draw3D (self):
       
        win = GraphWin("Cubo 3D",500,500)
        win.setCoords(-200, -200, 200, 200)
        
        point1 = Point(0,0)
        point2 = Point(self.getRadius,0)
        y = float((math.sqrt(3)/2) * 0.5 * self.getRadius)
        x = float(0.5*0.5*self.getRadius) + self.getRadius
        point3 = Point(x, y)
        point4 = Point(x, y + self.getRadius)
        point5 = Point(float(0.5*0.5*self.getRadius), y + self.getRadius)
        point6 = Point(0, self.getRadius)
        point7 = Point(self.getRadius, self.getRadius)
        line1 = Line(point1, point2)
        line2 = Line(point2, point3)
        line3 = Line(point3, point4)
        lina4 = Line(point4, point5)
        line5 = Line(point5, point6)
        line6 = Line(point6, point1)
        line7 = Line(point6, point7)
        line8 = Line(point7, point2)
        line9 = Line(point7, point4)
        
        line1.draw(win)
        line2.draw(win)
        line3.draw(win) 
        lina4.draw(win) 
        line5.draw(win) 
        line6.draw(win) 
        line7.draw(win) 
        line8.draw(win) 
        line9.draw(win)
        
        win.getMouse()
        win.close()
        
        
        
        
print("Digite o Valor da aresta do cubo")
n = float(input())

a = cubo(n)
print(f"Aresta = {a.aresta()}, Área da Face = {a.faceArea()} , Área da Superfície = {a.surfaceArea()}, Volume = {a.volume()}")

print(a.draw3I())
print(a.draw3D())
