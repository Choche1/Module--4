# Jorge Reyes
# November 15, 2022
# CSS 225
# leapyear variable
def is_leap(year):
  leap = False
  if (year % 4 == 0) and (year % 100 != 0):
      # code will be true if it is not..
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):

      leap = True
  else:
      leap = False

  return leap
# years needed
years = [ 1940, 1900, 1992, 1978, 2004, 2032, 2022, 2026, 2000, 2018, 1720]
leap_years = []
for year in years:
    print(is_leap(year))
    if is_leap(year):
        leap_years.append(year)
print(leap_years)


