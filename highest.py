# Jorge Reyes
# November 15, 2022
# CSS 225

# program to find the largest
# number among the three numbers
import random
a = random.randint(1,30)
b = random.randint(1,30)
c = random.randint(1,30)
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest
print(maximum(a, b, c))