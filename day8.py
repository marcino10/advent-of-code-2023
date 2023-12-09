import re

input_file = open("./inputs/day8.txt")
data = input_file.readlines()
input_file.close()

for x in range(len(data)):
    data[x] = data[x].replace('\n', '')

instruction = data[0]
instruction = instruction.replace('L', '0')
instruction = instruction.replace('R', '1')
data.pop(0)
data.pop(0)

coords = {}
for line in data:
    key = re.search(r"\w{3}", line).group()
    value1 = re.search(r"(?<=\()\w{3}", line).group()
    value2 = re.search(r"(?<= )\w{3}", line).group()
    coords[key] = [value1, value2]

step = 0
current_coord = "AAA"
instruction_index = 0

while True:
    if current_coord == "ZZZ":
        break

    if instruction_index == len(instruction):
        instruction_index = 0

    current_coord = coords[current_coord][int(instruction[instruction_index])]
    step += 1
    instruction_index += 1

print(step)
