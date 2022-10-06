def collatz(i):
    try:
        i = int(i)
    except:
        print('invalid input, need whole number')
        quit()
    while i != 1 and i != 0:
        if i%2 == 0:
            i = i/2
            print(i)
            continue
        elif i%2 != 0:
            i = 3*i+1
            print(i)
            continue
name = input('num?')
collatz(name)
