import re
i = open("regexexercisedata.txt").read()
i = re.findall("[0-9]+",i)

x = 0
for numbers in i:
    numbers = int(numbers)
    x += numbers

print(x)
