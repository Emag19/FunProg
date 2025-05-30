from graphics import *
import random

class Button(): # Classe dos botões
    def __init__(self,win, center, width, height, label, cor="green"):
        x, y = center.getX(), center.getY()
        self.rect = Rectangle(Point(x - width / 2, y - height / 2), Point(x + width / 2, y + height / 2))
        self.rect.setFill(cor)
        self.rect.draw(win)
        self.label = label
        self.text = Text(center, label)
        self.text.draw(win)
    

    def is_inside(self, pt): # Verificar se foi clicado
        p1 = self.rect.getP1()
        p2 = self.rect.getP2()
        return p1.getX() <= pt.getX() <= p2.getX() and p1.getY() <= pt.getY() <= p2.getY()



def main():
    win = GraphWin("Three Button Monte", 400, 400)
    win.setBackground("white")
    
    # Titlo
    title = Text(Point(200, 30), "Click a door to find the prize!")
    title.setSize(14)
    title.draw(win)
    
    # Cria 3 botões
    buttons = []
    labels = ["Door 1", "Door 2", "Door 3"]

    
    for i in range(3):
        btn = Button(win, Point(100+100*i, 200), 80, 160, labels[i])
        buttons.append(btn)
    
    
    win_counter = 0
    loss_counter = 0
    
    
    counter_text = Text(Point(200, 80), "Wins: 0  Losses: 0")
    counter_text.setSize(12)
    counter_text.draw(win)
    
    result_text = Text(Point(200, 350), "")
    result_text.setSize(12)
    result_text.draw(win)
    
    close = Button(win, Point(370, 60), 55, 55, "Fechar", "red")
        
    while True:
        # Escolhe um vencedor à toa
        winning_index = random.randint(0, 2)
        winner = labels[winning_index]
        
        click = win.getMouse()
        if close.is_inside(click):
            break
        escolha = None
        # Determinar o botão que foi clicado
        for btn in buttons:
            if btn.is_inside(click):
                escolha = btn

        
        if escolha is None:
            result_text.setText("You missed the doors! Try again.")

        elif winner == escolha.label:
            result_text.setText("You won!" + winner + " had the prize.")
            win_counter += 1
            
        else:
            result_text.setText("Sorry, you lost." + winner + " had the prize. Try again.")
            loss_counter += 1
         
        counter_text.setText("Wins: {}  Losses: {}".format(win_counter,loss_counter))   
         
    win.close()

main()
