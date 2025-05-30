from graphics import *
import random

class Button(): # Classe dos botões
    def __init__(self,win, center, width, height, label):
        x, y = center.getX(), center.getY()
        self.rect = Rectangle(Point(x - width / 2, y - height / 2), Point(x + width / 2, y + height / 2))
        self.rect.setFill("green")
        self.rect.draw(win)
        self.label = label
        self.text = Text(center, label)
        self.text.draw(win)
        self.win = False
    

    def is_inside(self, pt): # Verificar se foi clicado
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        return p1.getX() <= pt.getX() <= p2.getX() and p1.getY() <= pt.getY() <= p2.getY()



def main():
    win = GraphWin("Three Button Monte", 400, 300)
    win.setBackground("white")
    
    # Titlo
    title = Text(Point(200, 30), "Click a door to find the prize!")
    title.setSize(14)
    title.draw(win)
    
    # Cria 3 botões
    buttons = []
    labels = ["Door 1", "Door 2", "Door 3"]

    
    for i in range(3):
        btn = Button(win, Point(100+100*i, 150), 80, 160, labels[i])
        buttons.append(btn)
    
    # Escolhe um vencedor à toa
    winning_index = random.randint(0, 2)
    buttons[winning_index].win = True
    winning_label = buttons[winning_index].label
    
    result_text = Text(Point(200, 250), "")
    result_text.setSize(12)
    result_text.draw(win)
        
    while True:
        
        click = win.getMouse()
        escolha = None
        # Determinar o botão que foi clicado
        for btn in buttons:
            if btn.is_inside(click):
                escolha = btn

        
        if escolha is None:
            result_text.setText("You missed the doors! Try again.")

            
        elif escolha.win:
            result_text.setText("You won!" + winning_label + " had the prize.")
            break
        else:
            result_text.setText("Sorry, you lost." + winning_label + " had the prize.")
            break
         
 
    # Espera o usuário clicar para sair
    exit_text = Text(Point(200, 280), "Click anywhere to exit.")
    exit_text.setSize(10)
    exit_text.draw(win)
        
    win.getMouse()
    win.close()

main()
