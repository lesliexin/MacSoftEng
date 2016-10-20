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
    
    wRect = Rectangle(Point(435, 150), Point(645, 200))
    wRect.draw(window)
    wRect.setFill("white")
    wRect.setOutline("white")

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

    # fills square and moves it

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
