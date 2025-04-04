# button.py
# A simple Button widget.

from graphics import *

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """Creates a rectangular button, e.g.:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit')"""

        r = radius
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + r, x - r
        self.ymax, self.ymin = y + r, y - r
        self.circle = Circle( center,r)
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """RETURNS true if button active and p is inside."""
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        """RETURNS the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = 1

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = 0


