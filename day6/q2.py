import re

def q1():
    f = open('input-2.txt', 'r')
    space_regx = re.compile('[ ]+')

    time = time_parser(f.readline(), space_regx)
    distance = distance_parser(f.readline(), space_regx)

    ways = two_ways_search(time, distance)
    print('res: ' + str(ways))










def two_ways_search(time, record):
    left, right = 1, time-1
    ways = 0
    while left <= right:
        time_left = time - left
        speed_left = left
        distance_left = time_left * speed_left
        if distance_left > record:
            ways += 1

        time_right = time - right
        speed_right = right
        distance_right = time_right * speed_right
        if distance_right > record and left != right:
            ways += 1

        left += 1
        right -= 1
    return ways


def time_parser(line, space_regx):
    return int(re.sub(space_regx, '', re.sub(re.compile('Time:'), '', line)))


def distance_parser(line, space_regx):
    return int(re.sub(space_regx, '', re.sub(re.compile('Distance:'), '', line)))


if __name__ == '__main__':
    q1()