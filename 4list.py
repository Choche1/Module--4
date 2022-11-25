# Jorge Reyes
# November 15, 2022
# CSS 225

import random
import random
# create an empty list
lis = []
for _ in range(5):
    # create the range needed
    lis.append(random.randint(1,5))
for number in lis:
    # create forloop
    if number == 4:
        print(True)
    else:
        print(False)
#         create if and else statements
print(lis)