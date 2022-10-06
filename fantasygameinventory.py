#This program will nicely print out the given inventory

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def inventorydescription(x):
    count = 0
    for k, v in x.items():
        print(v,k)
        count += int(v)
    print('Total number of items:', count)

print(inventorydescription(inventory))
