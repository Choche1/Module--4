# Jorge Reyes
# November 15, 2022
# CSS 225

import random
# import random module
x = random.randint(1,20)
y = random.randint(1,20)
# create random range variables
i = 1
# create forloop for equation
while x!= y:
    i=(i+1)
    print("Numbers are not equal")
    x = random.randint(1,20)
    print("x equals", x)
#     print the true and false statements
# print the repetitions
print(x, "equals", y )
print("Are found after",i,"repetitions")