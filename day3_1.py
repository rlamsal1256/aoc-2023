import re

with open('day3.txt') as f:
    input = f.read().splitlines()

# input = [
#     '467..114..',
#     '...*......',
#     '..35..633.',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..',
# ]

# input = [
#     '.......',
#     '725.193',
#     '...*...',
# ]

def is_symbol(char):
    return bool(re.match(r'[^0-9.]', char))

def is_valid_coordinate(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def test(y_begin, y_end):
    # print(y_begin, y_end)
    
    no_adjacent_symbols = True
    for dx in [-1, 0, 1]:
        for dy in range(y_begin - 1 , y_end + 2):
            new_x, new_y = x + dx, dy
            if is_valid_coordinate(new_x, new_y, rows, cols):
                if is_symbol(input[new_x][new_y]):
                    no_adjacent_symbols = False
                    break
    
    return no_adjacent_symbols

rows = len(input)
cols = len(input[0])
sum = 0

for x in range(rows):
    number = ''
    y_begin = ''
    y_end = ''
    for y in range(cols):
        if input[x][y].isdigit():
            if not number:
                y_begin = y 
            number += str(input[x][y])

            if y == cols - 1:
                no_adjacent_symbols = test(y_begin, y)
                if not no_adjacent_symbols:
                    sum += int(number)

                number = ''
                y_begin = ''
                y_end = ''
        else:
            if number:
                y_end = y - 1
                no_adjacent_symbols = test(y_begin, y - 1)
                if not no_adjacent_symbols:
                    sum += int(number)

                number = ''
                y_begin = ''
                y_end = ''

print(sum)
