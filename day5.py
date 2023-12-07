import re

input_file = open("./inputs/day5.txt")
data = input_file.read()
input_file.close()

data = re.split(r"\n(?=.)(?!\d)", data)

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

# Solution for part 1
src_nums_part1 = src_nums.copy()
for instruction_map in data:
    tmp_src_nums = []
    unused_src_nums = src_nums_part1.copy()
    for instruction in instruction_map:
        start_dest = instruction[0]
        start_src = instruction[1]
        num_range = instruction[2]

        for num in src_nums_part1:
            if num in range(start_src, start_src + num_range):
                tmp_src_nums.append(start_dest + (num - start_src))
                unused_src_nums.remove(num)

    for num in unused_src_nums:
        tmp_src_nums.append(num)
    src_nums_part1 = tmp_src_nums

print(min(src_nums_part1))

# Solution for part 2
for instruction_map in data:
    changed_nums = []

    for instruction in instruction_map:
        start_dest = instruction[0]
        start_src = instruction[1]
        num_range = instruction[2]

        new_nums = 0
        current_num = 0
        while current_num < len(src_nums) - new_nums:
            min_num = src_nums[current_num]
            src_range = src_nums[current_num + 1]

            if min_num <= start_src < (min_num + src_range) or min_num <= start_src + num_range <= (
                    min_num + src_range) or (start_src < min_num < (start_src + num_range - 1)):

                src_nums.pop(current_num)
                src_nums.pop(current_num)

                if start_src - min_num > 0:
                    new_nums += 2
                    current_range = start_src - min_num
                    src_nums.append(min_num)
                    src_nums.append(current_range)
                    min_num = start_src
                    src_range -= current_range

                end_src = start_src + num_range - 1
                max_num = min_num + src_range - 1

                changed_nums.append(start_dest + (min_num - start_src))
                if end_src < max_num:
                    current_range = end_src - min_num + 1
                    changed_nums.append(current_range)
                    min_num = end_src + 1
                    src_range -= current_range
                else:
                    changed_nums.append(src_range)

                if min_num + src_range > start_src + num_range:
                    new_nums += 2
                    src_nums.append(min_num)
                    src_nums.append(src_range)
            else:
                current_num += 2

    src_nums.extend(changed_nums)

print(min(src_nums[0::2]))
