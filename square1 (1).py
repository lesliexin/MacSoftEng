from graphics import *
import math

X=1000
Y=500
rad=15

def inCircle(p,cir):
    px=p.getX()
    py=p.getY()
    r=cir.getRadius()
    c=cir.getCenter()
    cx=c.getX()
    cy=c.getY()
    if (((px - cx)**2 + (py - cy)**2) <= r**2):
        return True
    else:
        return False
    
def main():
    w=GraphWin("Sliding",X,Y)

    r=Rectangle(Point(0,400),Point(100,500))
    r.setOutline("black")
    r.draw(w)

    c1 = Circle(Point(450,170),rad)
    c1.setOutline("black")
    c1.setFill("red")
    c1.draw(w)

    c2 = Circle(Point(500,170),rad)
    c2.setOutline("black")
    c2.setFill("blue")
    c2.draw(w)

    c3 = Circle(Point(550,170),rad)
    c3.setOutline("black")
    c3.setFill("yellow")
    c3.draw(w)

    while True:
        click = w.getMouse()
        if (inCircle(click, c1)):
            r.setFill("red")
            break
        elif (inCircle(click, c2)):
            r.setFill("blue")
            break
        elif (inCircle(click, c3)):
            r.setFill("yellow")
            break

    while (r.getP2().getX()<=1000):
          r.move(5,0)

    w.getMouse()
        
    w.close()
    
main()
