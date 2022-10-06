num = input("Enter a number, and for all natural numbers below it I will print it if it's divisible by 3 or 5:")

x = 0
num = int(num)
for numbers in range(num):
    if numbers%3 == 0:
        print(numbers)
        continue
    elif numbers%5 == 0:
        print(numbers)
    else:
        continue

print(x)
