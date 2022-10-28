#Jorge Reyes
#Css 225



for i in range(1,50):
#this is the range of numbers
    if (i % 21 == 0):
        print("Divisible by both")
#if the range number is divisble by 7 and 3 it will print out "divisible by both"
    elif (i%3==0):
        print("Divisible by three")
#if divisible by 3 will print "divisble by 3"
    elif (i%7==0):
        print("Divisible by seven")
#if divisible by 7 will print out "divisible by 7"
    else:
        print(i)
#anything else will be displayed