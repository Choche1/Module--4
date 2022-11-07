#Jorge Reyes
#Novemeber 2, 2022
#CSS 225
#convert a user input value in radians to the value in degrees
import math
#import math module
facnum = int(input("Insert number"))
answer = 1
#ask for user input in radians
for i in range(1,facnum+1):
    answer = i*answer
#insert radian to degree formula
print(answer)
print(math.factorial(facnum))

