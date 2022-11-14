#Jorge Reyes
#CSS_225
#November 10, 2022
#import random functions and module
import random
#create a range between 1,10
range_1 = range(1,10)
for i in range(20):
#give i a variable
#use random mod for random range
    randr=random.randrange(1,16)
    if randr in range_1:
        print(randr, 'is present in the range.')
    else:
        print(randr, 'is not present in the range.')
#if and else statement wether random number is range or not