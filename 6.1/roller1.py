# roller . py
# Graphics program to roll a pair of dice . Uses custom widgets
# Button and DieView .
from random import randrange
from graphics import GraphWin, Point
from CButton import Button
from dieview import DieView
def main():
    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("blue")
    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = Button(win, Point(5,4.5), 1.65, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5,1), 1.1, "Quit")
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            
            value2 = randrange(1, 7)
            die2.setValue(value2)
            
            quitButton.activate()
        
        pt = win.getMouse()  # Aguarda próximo clique
    
    win.close()
    
main()
