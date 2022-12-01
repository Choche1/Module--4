# Jorge Reyes
# CSS225

# Program Name: branching.py
# Purpose of a program: A time traveler has suddenly appeared in your classroom!
# The travelor enters his/her year of origin
# Program returns a greeting message according to the year.
# Distant Past: Before 1900
# Present Era-Years between 1900-2020
# Far Future: After 2020

# Total errors 7

year = int(input("Greetings! What is your year of origin? "))
# SyntaxError: unterminated string literal (detected at line 9)
# SyntaxError: unmatched ')'
# SyntaxError: expected :':'
if year <= 1900:
    # NameError: name 'year' is not defined
    print ("Woah, that's the past!")
#     SyntaxError: unterminated string literal (detected at line 14)
elif year > 1900 and year < 2020:
    # SyntaxError: invalid syntax
    print ("That's totally the present!")
#     SyntaxError: invalid syntax
else:
    print ("Far out, that's the future!!")
