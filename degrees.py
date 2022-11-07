#Jorge Reyes
#Novemeber 2, 2022
#CSS 225
#convert radians to degrees
import math
#import math module
radnum = float(input("Insert radian"))
numdegrees = 360/(2*math.pi)*radnum
#convert from radians to degrees
print(numdegrees)
print(math.degrees(radnum))