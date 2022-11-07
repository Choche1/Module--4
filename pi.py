#Jorge Reyes
#Novemeber 2, 2022
#CSS 225
#this is a program that approximates π according to the Leibniz’s formula
import math
#import math module
pi = 0
denom = 1
#give pi and denom a variable
for i in range(0,1000001):
    if i %2 == 0:
        pi = pi +4/denom
    else:
        pi = pi - 4/denom
    denom = denom +2
#create a forloop  with a if and else statement
print("PI=",pi)
print(math.pi)
#print results