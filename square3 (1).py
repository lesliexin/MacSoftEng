from graphics import *
import math

X=1000
Y=500
rad=15

def selectColour(ck,c1_,c2_,c3_,r_): #changes the colour of the square
    while True:
        if (inCircle(ck, c1_)):
            r_.setFill("red")
            break
        elif (inCircle(ck, c2_)):
            r_.setFill("blue")
            break
        elif (inCircle(ck, c3_)):
            r_.setFill("yellow")
            break
    return ()
    
def inCircle(p,cir): #returns whether the click is within a button
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
    #window
    w=GraphWin("Sliding",X,Y)

    #creating the square
    r=Rectangle(Point(0,400),Point(100,500))
    r.setOutline("black")
    r.draw(w)

    #radio button 1 (red)
    c1 = Circle(Point(450,170),rad)
    c1.setFill("red")
    c1.draw(w)

    #radio button 2 (blue)
    c2 = Circle(Point(500,170),rad)
    c2.setFill("blue")
    c2.draw(w)

    #radio button 3 (yellow)
    c3 = Circle(Point(550,170),rad)
    c3.setFill("yellow")
    c3.draw(w)

    #1st colour change
    click = w.getMouse()
    selectColour(click,c1,c2,c3,r)

    #square moves to centre
    while (r.getP2().getX()<=550):
          r.move(5,0)

    #square jumps 
    while (r.getP2().getY()>=350):
          r.move(0,-5)

    #2nd colour change
    click = w.getMouse()
    selectColour(click,c1,c2,c3,r)

    #square lowers
    while (r.getP2().getY()<=500):
          r.move(0,5)
          
    #square moves to end
    while (r.getP2().getX()<=1000):
          r.move(5,0)

    w.getMouse()
        
    w.close()
    
main()
