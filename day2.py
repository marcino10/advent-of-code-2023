import re

input_file = open("./inputs/day2.txt")
data = input_file.readlines()
input_file.close()

current_id = 1
sum_id = 0
sum_powers = 0

for game in data:
    game_regex = re.search("(Game [0-9]*): ", game)
    game = game.replace(game_regex.group(), '')
    game = game.replace("\n", "")

    subsets = re.split("[,;] ", game)
    sorted_by_colors = {'red': [], 'green': [], 'blue': []}
    is_possible = True

    for grab in subsets:
        num_of_cubes = int(re.search(r"\d+", grab).group())
        color_of_cube = re.search(r"red|green|blue", grab).group()
        sorted_by_colors[color_of_cube].append(num_of_cubes)

    min_red, min_green, min_blue = 0, 0, 0

    for num in sorted_by_colors['red']:
        if num > 12:
            is_possible = False
        if num > min_red:
            min_red = num

    for num in sorted_by_colors['green']:
        if num > 13:
            is_possible = False
        if num > min_green:
            min_green = num

    for num in sorted_by_colors['blue']:
        if num > 14:
            is_possible = False
        if num > min_blue:
            min_blue = num

    if is_possible:
        sum_id += current_id

    power_of_set = min_red * min_green * min_blue
    sum_powers += power_of_set
    current_id += 1

print(sum_id)
print(sum_powers)
