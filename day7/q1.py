import re
from collections import Counter

letter_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
              '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
              '3': 3, '2': 2}



def q1():
    f = open('input.txt', 'r')
    space_regx = re.compile('[ ]+')
    card_arr = []

    for line in f.readlines():
        splitter_arr = re.split(space_regx, line)
        card, val = splitter_arr[0], int(splitter_arr[1])
        card_arr.append((card, val, comparator(card)))

    print(card_arr)
    card_arr.sort(key=lambda x: x[2])
    print(card_arr)

    res = 0
    for idx, arr in enumerate(card_arr):
        res += (idx + 1) * arr[1]
    print(res)


def comparator(card):
    val = 0
    freq_d = Counter(card)
    freq_arr = []
    for key, value in freq_d.items():
        freq_arr.append([key, value])
    freq_arr.sort(key=lambda x: x[1])

    for letter, freq in freq_d.items():
        val += 10 ** freq

    seed = 0.01
    for idx, letter in enumerate(card):
        val += letter_map[letter] * seed
        seed = seed / 100

    return val


if __name__ == '__main__':
    q1()
