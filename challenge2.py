from graphics import *

height = 500
width = 1000
radius = 15

def main():

    # creating window and drawing/filling objects

    window = GraphWin("Challenge 1", width, height)

    square = Rectangle(Point(0, 400), Point(100, 500))
    square.draw(window)

    circle1 = Circle(Point(450, 170), radius)
    circle1.setFill("red")
    circle1.setOutline("red")
    circle1.draw(window)

    circle2 = Circle(Point(500, 170), radius)
    circle2.setFill("blue")
    circle2.setOutline("blue")
    circle2.draw(window)

    circle3 = Circle(Point(550, 170), radius)
    circle3.setFill("yellow")
    circle3.setOutline("yellow")
    circle3.draw(window)

    # add text on top of buttons
    
    message1 = Text(Point(500,100), "Choose the color of the square and start it rolling")
    message1.setTextColor("blue")
    message1.draw(window)
    message1.setStyle("bold")
    message1.setSize(14)
    
    message2 = Text(Point(500,120), "by clicking on one of the three radio buttons")
    message2.setTextColor("blue")
    message2.draw(window)   
    message2.setStyle("bold")
    message2.setSize(14)
    
    # getting click position until overlapping a radio button

    color = "grey"

    while (color == "grey"):

        click = window.getMouse()

        if inside(click, circle1):
            color = "red"
        elif inside(click, circle2):
            color = "blue"
        elif inside(click, circle3):
            color = "yellow"

    # fills square and moves it

    square.setFill(color)
    square.setOutline(color)

    # hides buttons before moving
    
    wRect = Rectangle(Point(300, 80), Point(800, 200))
    wRect.setOutline("white")
    wRect.setFill("white")
    wRect.draw(window)

    # move square to the centre
    
    while square.getP2().getX() <= 550:
        square.move(5, 0)

    # show buttons
    
    wRect.undraw()

    # getting click position until overlapping a radio button

    color = "grey"
    while (color == "grey"):

        click = window.getMouse()

        if inside(click, circle1):
            color = "red"
        elif inside(click, circle2):
            color = "blue"
        elif inside(click, circle3):
            color = "yellow"

    # fills square

    square.setFill(color)
    square.setOutline(color)

    # hides buttons before moving
    
    wRect.draw(window)

    # move square to end
    
    while square.getP2().getX() <= 1000:
        square.move(5, 0)

    # closes program

    window.getMouse()

    window.close()

def inside(click, circle):

    # uses pythagorean theoreum to determine if click is within circle

    clickX = click.getX()
    clickY = click.getY()

    circleX = circle.getCenter().getX()
    circleY = circle.getCenter().getY()

    distance = ((clickX - circleX)**2 + (clickY - circleY)**2)**.5

    if distance <= circle.getRadius():
        return True
    else:
        return False

main()
