import re

input_file = open("./inputs/day7.txt")
data = input_file.read()
input_file.close()


def compare_values(hand, sorted_hand, current_char):
    if cards_value[hand[current_char]] > cards_value[sorted_hand[current_char]]:
        index = tmp_sorted_hands.index(sorted_hand)
        tmp_sorted_hands.insert(index, hand)
        return True
    elif cards_value[hand[current_char]] == cards_value[sorted_hand[current_char]]:
        current_char += 1
        if compare_values(hand, sorted_hand, current_char):
            return True


def sort_hands(hands):
    global tmp_sorted_hands
    tmp_sorted_hands = [hands[0]]
    for hand in hands[1:]:
        for sorted_hand in tmp_sorted_hands:
            if compare_values(hand, sorted_hand, 0):
                break
        if hand not in tmp_sorted_hands:
            tmp_sorted_hands.append(hand)
    return tmp_sorted_hands


def append_sorted_hands(deck):
    if deck:
        deck = sort_hands(deck)
        for hand in deck:
            sorted_hands.append(hand)


cards_value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
               '2': 2}

hands = re.findall(r"\w{5}(?= )", data)
bids = re.findall(r"(?<= )\d+", data)

num_of_hands = len(hands)
five_hands = []
four_hands = []
full_hands = []
three_hands = []
two_hands = []
one_hands = []
high_hands = []

hand_to_bids = {}
bid_index = 0
for hand in hands:
    num_of_card = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0,
                   '2': 0}

    for card in hand:
        num_of_card[card] += 1

    three_cards = 0
    pair_cards = 0
    is_assign = False
    for card_key in num_of_card:
        if num_of_card[card_key] == 5:
            five_hands.append(hand)
            is_assign = True
            break
        elif num_of_card[card_key] == 4:
            four_hands.append(hand)
            is_assign = True
            break
        if num_of_card[card_key] == 3:
            three_cards += 1
        if num_of_card[card_key] == 2:
            pair_cards += 1

    if not is_assign:
        if three_cards == 1 and pair_cards == 1:
            full_hands.append(hand)
        elif three_cards == 1:
            three_hands.append(hand)
        elif pair_cards == 2:
            two_hands.append(hand)
        elif pair_cards == 1:
            one_hands.append(hand)
        else:
            high_hands.append(hand)

    hand_to_bids[hand] = bids[bid_index]
    bid_index += 1

sorted_hands = []
append_sorted_hands(five_hands)
append_sorted_hands(four_hands)
append_sorted_hands(full_hands)
append_sorted_hands(three_hands)
append_sorted_hands(two_hands)
append_sorted_hands(one_hands)
append_sorted_hands(high_hands)

total_win = 0
rank = 1
for hand in sorted_hands[::-1]:
    total_win += rank * int(hand_to_bids[hand])
    rank += 1

print(total_win)
