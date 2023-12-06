import re

def q1():
    f = open('input.txt', 'r')
    lines = f.readlines()
    map_regx = re.compile("[-a-z]+ map:")

    seeds = []
    conversion_map_arr = []
    conversion_map_individual_arr = []
    for idx, line in enumerate(lines):
        if idx == 0:
            seeds = seeds_parser(line)
            print('seeds: ' + str(seeds))
        elif line == '\n' or re.match(map_regx, line):
            if len(conversion_map_individual_arr) != 0:
                conversion_map_arr.append(conversion_map_individual_arr)
            conversion_map_individual_arr = []
            continue
        else:
            arr = conversion_parser(line)
            conversion_map_individual_arr.append(arr)
    print(conversion_map_arr)

    res = float('inf')
    for seed in seeds:
        # print('seed start converting: ' + str(seed))
        nxt_num = seed
        for idx, arr in enumerate(conversion_map_arr):
            for boundary_arr in arr:
                left, right, base = boundary_arr[0], boundary_arr[1], boundary_arr[2]
                if left <= nxt_num < right:
                    nxt_num = nxt_num - left + base
                    break
            # print(str(idx) + ' time converting res: ' + str(nxt_num))
        res = min(nxt_num, res)
    print('res: ' + str(res))











def seeds_parser(line):
    return [int(numeric_str) for numeric_str in re.sub(re.compile('seeds: '), '', line).strip().split(' ')]


def conversion_parser(line):
    # print(line)
    tmp_arr = [int(numeric_str) for numeric_str in line.split(' ')]
    return [tmp_arr[1], tmp_arr[1]+tmp_arr[2], tmp_arr[0]]


if __name__ == '__main__':
    q1()