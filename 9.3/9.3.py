from graphics import *

def main():
    win = GraphWin("9.2",500 ,500, autoflush=False)
    image = Image(Point(250,250),"lago.ppm") #256x256
    image_height = image.getHeight() #y
    image_width = image.getWidth() #x
    
    pedido = Text(Point(250,400),"Converter a imagem para tons inversos? (Clilca para continuar)")
    pedido.draw(win)
    win.getMouse()
    pedido.undraw()
    image.draw(win)
    
    for y in range(image_height):
        for x in range(image_width):
            red, green, blue = image.getPixel(x, y)
            ired = 255 - red
            iblue = 255 - blue
            igreen = 255 - green
            image.setPixel(x, y, color_rgb(ired, igreen, iblue))
        update(75)
    
    guardar = Text(Point(250,400),"Guardar a imagem?" )
    guardar.draw(win)
    win.getMouse()
    guardar.undraw()
    
    nome = input()
    image.save(nome)
    
    
    win.getMouse()
    win.close()

main()