#Jorge Reyes
#Css 225
#October 27, 2022
# asks the user for the number of sides, the length of the side,the color of the line, and the fill color of a regular polygon
import turtle
#this imports turtle module


s = turtle.Screen()
#this sets the screen graphics window

t = turtle.Turtle()
#provides primitives needed in the program
sides = int(input("Enter the number of sides: "))
#this gets the number of sides

length = int(input("Enter the length of the side: "))
#this gets the length of each sides
col = input("Enter the color of your polygon: ")
#this gets the color of fill
t.fillcolor(col)
#this fills the color
t.begin_fill()
#this begins the fill
#this begins the the iteration drawing
for x in range(sides):

   t.forward(length)

   t.right(360/sides)

t.end_fill()

s.mainloop()
#this ends the fill