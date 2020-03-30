def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        first = list.pop(0)
        return first + sum(list)


print(sum([2, 4, 6]))


def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])


print(count([2, 4, 6]))


def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(max([2, 4, 6]))
