# Program Name: pirate.py
# Purpose of a program:
# User can be screened by the greeting message user enters as: a pirate or pirate hater
# Pirates greet each other with a password.
# If the greeting is matched to Arrr!,the user is identified as a pirate.
# Otherwise, the user is a hater of pirates.
# Jorge Reyes
# CSS 225
#error 3
# SyntaxError: unterminated string literal (detected at line 8)
greeting = input("Hello, possible pirate! What's the password?")
if greeting in "Arrr!":
	# SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
	print("Go away, pirate.")
# SyntaxError: invalid syntax
else:
	print("Greetings, hater of pirates!")
