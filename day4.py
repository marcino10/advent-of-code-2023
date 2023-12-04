import re

input_file = open("./inputs/day4.txt")
data = input_file.readlines()
input_file.close()

sum_points = 0
num_of_cards = {}
sum_cards = 0

for card in range(1, len(data) + 1):
    num_of_cards[str(card)] = 1

for card in range(1, len(data) + 1):
    card_pattern = re.search(r"Card *\d+: ", data[card - 1]).group()
    data[card - 1] = data[card - 1].replace(card_pattern, '')

    nums = data[card - 1].split('|')
    win_nums = re.findall(r"\d+", nums[0])
    draw_nums = re.findall(r"\d+", nums[1])

    points = 0
    win_cards = 0
    for num in draw_nums:
        if num in win_nums:
            win_cards += 1
            if points == 0:
                points += 1
            else:
                points *= 2

    for x in range(1, win_cards + 1):
        num_of_cards[str(card + x)] += num_of_cards[str(card)]

    sum_points += points
    sum_cards += num_of_cards[str(card)]

print(sum_points)
print(sum_cards)
