import re

input_file = open("./inputs/day3.txt")
data = input_file.readlines()
input_file.close()

symbols_coords = []
sum_parts = 0
stars = {}
sum_gears = 0

for line in range(len(data)):
    data[line] = data[line].replace('\n', '')
    for char in range(len(data[line])):
        if re.search(r'[^.0-9]', data[line][char]):
            symbols_coords.append([line, char])
            if data[line][char] == '*':
                stars[f"{line},{char}"] = []

for line in range(len(data)):
    nums = re.findall(r'\d+', data[line])
    last_coords = 0

    for num in nums:
        num_coords = list(re.search(num, data[line][last_coords:]).span())
        num_coords[0] += last_coords
        num_coords[1] += last_coords
        last_coords = num_coords[1] - 1

        for coords in symbols_coords:
            if coords[0] in range(line - 1, line + 2) and coords[1] in range(num_coords[0] - 1, num_coords[1] + 1):
                sum_parts += int(num)
                if f'{coords[0]},{coords[1]}' in stars:
                    stars[f'{coords[0]},{coords[1]}'].append(int(num))

for star in stars:
    if len(stars[star]) == 2:
        sum_gears += stars[star][0] * stars[star][1]

print(sum_parts)
print(sum_gears)
