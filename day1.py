input_file = open("./inputs/day1.txt")
data = input_file.readlines()
input_file.close()

sum_values = 0
str_digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
              'nine': '9'}

for line in data:
    first_num, second_num = None, None
    first_num_index = len(line)
    second_num_index = -1

    for x in range(len(line) - 1):
        if line[x].isdigit():
            if first_num is None:
                first_num = line[x]
                first_num_index = x
            else:
                second_num = line[x]
                second_num_index = x

    if second_num is None and first_num is not None:
        second_num = first_num
        second_num_index = first_num_index

    for key in str_digits:
        if key in line:
            if line.find(key) < first_num_index:
                first_num = str_digits[key]
                first_num_index = line.find(key)
            if line.rfind(key) > second_num_index:
                second_num = str_digits[key]
                second_num_index = line.rfind(key)

    sum_values += int(first_num + second_num)

print(sum_values)
