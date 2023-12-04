import re


def q2():
    f = open('q2_input.txt', 'r')
    regx = re.compile('Card[ ]+[0-9]+: ')
    space_regx = re.compile('[ ]+')
    lines = f.readlines()
    length = len(lines)
    copy_arr = [0 for i in range(length)]
    res = 0
    for idx, line in enumerate(lines):
        print(line)
        tmp = parse(idx, length, line, regx, space_regx, copy_arr)
        print('tmp' + str(tmp))
        print(copy_arr)
        res += tmp
    print(res)

def parse(idx, length, line, regx, space_regx, copy_arr):
    s_arr = re.sub(regx, '', line).split('|')
    s_1 = re.split(space_regx, s_arr[0].strip())
    s_2 = re.split(space_regx, s_arr[1].strip())

    winning_set = set(s_1)
    n = 0
    for s in s_2:
        if s in winning_set:
            n += 1
    print('n: ' + str(n))
    if n == 0:
        return copy_arr[idx] + 1
    else:
        bonus = 1 + copy_arr[idx]
        for i in range(1, n+1):
            copy_arr_idx = idx + i
            if copy_arr_idx < length:
                copy_arr[copy_arr_idx] += bonus
        return bonus

if __name__ == '__main__':
    q2()