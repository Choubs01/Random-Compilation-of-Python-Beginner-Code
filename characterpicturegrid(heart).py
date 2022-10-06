#This program will print and rotate the given list of lists 90 degrees clockwise

grid =  [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x = 0
y = 0
while True:
    try:
        print(grid[y][x], end='')
        y += 1
    except:
        x += 1
        y = 0
        print('')
    if x == 5 and y == 9:
        break
