from graphics import *
def main():
    win = GraphWin("Retangulo DIY", 400, 400)
    win.setCoords(0, 0, 50, 50)
    win.setBackground("#FFFF00")
    
    texto = Text(Point(25,25), "Clica em dois pontos")
    texto.draw(win)
    
    ponto1 = win.getMouse()
    ponto2 = win.getMouse()
    
    x1 = ponto1.getX()
    y1 = ponto1.getY()
    x2 = ponto2.getX()
    y2 = ponto2.getY()
    
    comprimento = abs(x2 - x1)
    largura = abs(y2 - y1)
    
    area = abs(comprimento * largura)
    Area = Text(Point(25,45), f"Area = {round(area)}" )
    Area.draw(win)
    
    perimetro = abs((comprimento * 2) + (largura * 2))
    Perimetro = Text(Point(25,48), f"Perimetro = {round(perimetro)}")
    Perimetro.draw(win)
    
    texto.undraw()
    Retangulo = Rectangle(ponto1, ponto2)
    Retangulo.draw(win)
    
    
    win.getMouse()
    win.close()

main()
    #Tomé Freitas 114112