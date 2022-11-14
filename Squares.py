#Jorge Reyes
#CSS_225
#November 10, 2022
import turtle
#import turtle mod
#create initial sqaurewith 4 sides
def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)
#90 degree angles
wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")
# drawSquare(alex,45)
#create a forloop for the next 5 squares
for i in range(1,5):
#angles and penup and down commands
    drawSquare(alex,i*20)
    alex.penup()
    alex.left(225)
    alex.forward(10)
    alex.pendown()
    alex.right(225)







wn.exitonclick()

