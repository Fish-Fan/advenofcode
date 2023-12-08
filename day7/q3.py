import sys
from collections import Counter
from functools import cmp_to_key

if __name__ == '__main__':
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


    def getType(hand: list[str]) -> int:
        count = Counter(hand)
        jcount = count.pop('J', 0)
        maxCard = max(count, key=count.get, default='')
        for _ in range(jcount):
            count[maxCard] = min(count[maxCard] + 1, 5)
        count = sorted(list(count.values()) + [jcount * (not maxCard)], reverse=True)
        if count[0] == 5:
            return 1
        elif count[0] == 4:
            return 2
        elif count[0:2] == [3, 2]:
            return 3
        elif count[0] == 3:
            return 4
        elif count[0:2] == [2, 2]:
            return 5
        elif count[0] == 2:
            return 6
        else:
            return 7


    def compare(hand1: list[str], hand2: list[str]) -> int:
        h1, h2 = hand1[0], hand2[0]
        type1, type2 = getType(h1), getType(h2)
        if type1 != type2:
            return type2 - type1
        for a, b in zip(h1, h2):
            if cards.index(a) < cards.index(b):
                return 1
            elif cards.index(a) > cards.index(b):
                return -1
        return 0

    f = open('input-2.txt')
    ls = [x.split() for x in f.readlines()]
    hands = sorted(ls, key=cmp_to_key(compare))
    for arr in hands:
        print(arr)
    ans = 0
    for i, bet in enumerate([int(x[1]) for x in hands]):
        ans += (i + 1) * bet
    print(ans)