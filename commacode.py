#This program will print the terms of a list while seperated by commas, and the last term will be preceded by a 'and'

lst = []
while True:
    spam = input(print('enter terms (enter stop to finish): ', end=''))
    if spam == 'stop':
        break
    lst.append(spam)

if len(lst) < 3:
    print('Too few terms')
    exit()

def listdescription(l):
    for terms in l[:-1]:
        print(terms + ', ', end='')
    print('and', l[-1])

listdescription(lst)
