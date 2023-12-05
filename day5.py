import re

input_file = open("./inputs/day5.txt")
data = input_file.read()
input_file.close()

data = re.split(r"\n(?=.)(?!\d)", data)

maps = []

for x in range(len(data)):
    data[x] = re.sub(r".*:[\n ]", '', data[x])
    if data[x][-1] == "\n":
        data[x] = data[x][:-1]
    data[x] = data[x].split('\n')

    for y in range(len(data[x])):
        data[x][y] = data[x][y].split(' ')
        for num in range(len(data[x][y])):
            data[x][y][num] = int(data[x][y][num])

src_nums = data[0][0]
del data[0]

for instruction_map in data:
    tmp_src_nums = []
    unused_src_nums = src_nums.copy()
    for instruction in instruction_map:
        start_dest = instruction[0]
        start_src = instruction[1]
        num_range = instruction[2]

        for num in src_nums:
            if num in range(start_src, start_src + num_range):
                tmp_src_nums.append(start_dest + (num - start_src))
                unused_src_nums.remove(num)

    for num in unused_src_nums:
        tmp_src_nums.append(num)
    src_nums = tmp_src_nums

print(min(src_nums))
