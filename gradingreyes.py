

exam_one = int(input("Input exam grade one: "))
# NameError: name 'exam_three' is not defined

exam_two = int(input("Input exam grade two: "))
# SyntaxError: unmatched ')'
exam_three = str(input("Input exam grade three: "))
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
    sum = sum + grade
# NameError: name 'grade' is not defined. Did you mean: 'grades'?
avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
# SyntaxError: expected ':'
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
#     SyntaxError: unterminated string literal (detected at line 21)
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"
# SyntaxError: invalid syntax

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)
# SyntaxWarning: "is" with a literal.
if letter_grade == "F":
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print ("Student is failing.")
# SyntaxError: Missing parentheses in call to 'print'.
else:
    print ("Student is passing.")
