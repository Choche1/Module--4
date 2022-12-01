# Program Name: time2.py
# Purpose of a program:
# User inputs current time and hours to wait.
# Then program returns the time user's waiting tiime ends.
# Jorge Reyes
# CSS 225
str_time = input("What time is it now?")
str_wait_time = input("What is the number of nours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)
# NameError: name 'wait_time' is not defined. Did you mean: 'wai_time'?
time_when_to_start = time + wait_time
print(time_when_to_start)
# NameError: name 'time_when_to_start' is not defined.