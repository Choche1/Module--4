#Jorge Reyes
#CSS_225
#November 10, 2022
#import turtle
import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()
#create original octagon
#add colorand pensize
sides=6
alex.color("pink")
alex.pensize(2)
#create a forloop to repeat 8 times to create flower
def drawHexagon(sides,):
    for i in range(sides):
        alex.forward(70)
        alex.left(360 / sides)

for i in range(8):
    alex.left(45)
    drawHexagon(6)


