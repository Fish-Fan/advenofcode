import re
def print_hi():
    f = open('q1_input.txt', 'r')
    regx = re.compile('Card[ ]+[0-9]+: ')
    space_regx = re.compile('[ ]+')
    lines = f.readlines()
    res = 0
    for line in lines:
        # print(line)
        tmp = parse(line, regx, space_regx)
        # print('tmp' + str(tmp))
        res += tmp
    print(res)

def parse(line, regx, space_regx):
    s_arr = re.sub(regx, '', line).split('|')
    s_1 = re.split(space_regx, s_arr[0].strip())
    s_2 = re.split(space_regx, s_arr[1].strip())

    winning_set = set(s_1)
    n = 0
    for s in s_2:
        if s in winning_set:
            n += 1
    # print('n: ' + str(n))
    if n == 0:
        return n
    else:
        return 2 ** (n-1)



if __name__ == '__main__':
    print_hi()