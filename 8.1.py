#8.1 - FunProg
from graphics import *

class GrupoGrafico:
    
    def __init__(self,ancora):
        self.ancora = ancora
        self.objetos = []
        
    def retornaAncora (self):
        return self.ancora.clone()
    
    def AdicionaObjeto(self,objeto):
        self.objetos.append(objeto)
    
    def move(self, dx, dy):
        self.ancora.move(dx,dy)
        for objeto in self.objetos:
            objeto.move(dx,dy)
    
    def desenha(self, win):
        for objeto in self.objetos:
            objeto.draw(win)
    
    def apaga (self):
        for objeto in self.objetos:
            objeto.undraw()

def main():
    win = GraphWin("8.1", 600, 600)
    ancora = Point(300,300)
    Grupo = GrupoGrafico(ancora)
    
    Circulo = Circle(ancora,50)
    Circulo.setFill("white")
    
    Circulo2 = Circle(ancora,25)
    Circulo2.setFill("black")
    
    Circulo3 = Circle(ancora,15)
    Circulo3.setFill("blue")
    
    Grupo.AdicionaObjeto(Circulo)
    Grupo.AdicionaObjeto(Circulo2)
    Grupo.AdicionaObjeto(Circulo3)

    Grupo.desenha(win)
    
    while True:
        click = win.getMouse()
        if click is None:
            break
        
        PontoCentral = Grupo.retornaAncora()
        dx = click.getX() - PontoCentral.getX()
        dy = click.getY() - PontoCentral.getY()

        Grupo.move(dx, dy)
        
        win.getMouse()
        Grupo.apaga()
        win.getMouse()
        win.close()
      
main()
            
    
    
            

            
        
        
        
        
        
        
        
        
        
        
    