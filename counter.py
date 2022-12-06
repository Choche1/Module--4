# Jorge Reyes
# CSS 225
counter = 20
tens = []
vowels = []
# lists
while counter <= 70:
    if(counter % 10 == 0):
        tens.append(counter)
    if(ord('A') == counter or ord('E') == counter or ord('I') == counter or ord('O') == counter or ord('U') == counter):
        vowels.append(counter)
    counter =+ 1
# results tens
for number in tens:
    print(number)
# results vowels
for character in vowels:
    print(character)

