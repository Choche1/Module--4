#Jorge Reyes
#CSS_225
#November 10, 2022
#give a list with the numbers provided
lst = [1, 3, 3, 3, 6, 2, 3, 6, 5, 4, 2]
uniq = []
#name the unique
for i in lst:
    if i not in uniq:
        uniq.append(i)
    else:
        pass
#make it so it weeds out the repeats
print(uniq)
# print(i)