import re

input_file = open("./inputs/day6.txt")
data = input_file.readlines()
input_file.close()


def get_result(races):
    result = 1
    for race in races:
        num_of_ways = 0
        time = race[0]
        record = race[1]

        speed = 1
        for way in range(1, time):
            if speed * (time - speed) > record:
                num_of_ways += 1
            speed += 1
        result *= num_of_ways
    print(result)


# Parsing for part 1
data_part1 = data.copy()

for x in range(len(data_part1)):
    data_part1[x] = re.findall(r"\d+", data_part1[x])

races = []
isTime = True
for line in data_part1:
    current_race = 0
    for num in line:
        if isTime:
            races.append([])
        races[current_race].append(int(num))
        current_race += 1
    isTime = False

get_result(races)

# Parsing for part 2
races = [[]]
for line in range(len(data)):
    data[line] = data[line].replace(' ', '')
    data[line] = data[line].replace('\n', '')
    only_digits = re.search(r"\D+", data[line]).group()
    data[line] = data[line].replace(only_digits, '')
    races[0].append(int(data[line]))

get_result(races)
