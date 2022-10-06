#Proving perfect square broot method

number = input('number:')
try:
    num = int(number)
except:
    print('whole number required')
for numbers in range(1, int(num/2)+1):
    if num == numbers*numbers:
        print('                           ','num is a ps')
    else:
        print('num is not a ps')
exit()
