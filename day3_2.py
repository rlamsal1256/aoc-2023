import re

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
#     '467..114..',
#     '...*......',
#     '..35..633.',
# ]

# input = [
#     '......755.',
#     '...$.*....',
#     '.664.598..',
# ]

# input = [
#     '..123.755.',
#     '...$.*....',
#     '.664......',
# ]

# input = [
#     '....123...',
#     '.....*....',
#     '....664...',
# ]

# input = [
#     '.......',
#     '855*...',
#     '....548',
# ]

# input = [
#     '123....',
#     '...*...',
#     '....548',
# ]

with open('day3.txt') as f:
    input = f.read().splitlines()

def is_symbol(char):
    return char == '*'

def is_valid_coordinate(x, y):
    return 0 <= x < rows and 0 <= y < cols

rows = len(input)
cols = len(input[0])

sum = 0
real_set = set()
for x in range(rows):
    for y in range(cols):
        if is_symbol(input[x][y]):
            list = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x, new_y = x + dx, y + dy
                    if is_valid_coordinate(new_x, new_y):
                        if input[new_x][new_y].isdigit():
                            list.append([new_x, new_y])
            part_numbers = set()
            for item in list:
                a, b = item
                number = str(input[a][b])
                new_b = b - 1
                while is_valid_coordinate(a, new_b) and input[a][new_b].isdigit():
                    number = f"{input[a][new_b]}{number}"
                    new_b -= 1
                new_b = b + 1
                while is_valid_coordinate(a, new_b) and input[a][new_b].isdigit():
                    number = f"{number}{input[a][new_b]}"
                    new_b += 1
                part_numbers.add(int(number))
            if len(part_numbers) == 2:
                real_set.add((part_numbers.pop(), part_numbers.pop()))

for item in real_set:
    sum += item[0] * item[1]

print(sum)
