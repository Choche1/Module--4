# Jorge Reyes
# CSS 225
userInput = input("Please enter a word: ")
# user input
userInputLength = len(userInput) - 1
finalWord = ""
# get last character of user input toss it in final word
while userInputLength >= 0:
    finalWord = finalWord + userInput[userInputLength]
    userInputLength -= 1

# print result
print(finalWord)