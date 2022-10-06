# This program will add the given list to the player's inventory

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

for items in dragonLoot:
    inventory[items] = inventory.get(items,0) + 1

def inventorydescription(x):
    count = 0
    for k, v in x.items():
        print(v,k)
        count += int(v)
    print('Total number of items:', count)

print(inventorydescription(inventory))
