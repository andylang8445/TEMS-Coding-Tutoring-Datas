import math

def mySorting(li: list):
    new_li = li.copy()
    flag = 0
    sorted_li = []
    for i in new_li:
        distance = math.sqrt(((i[0] * i[0]) + (i[1] * i[1])))
    while flag == 0:
        flag = 1
        tmp = [0, 0]
        max_distance = -1
        for i in new_li:
            distance = math.sqrt(((i[0] * i[0]) + (i[1] * i[1])))
            if distance > max_distance:
                tmp[0] = i[0]
                tmp[1] = i[1]
                max_distance = distance
                flag = 0
        if flag == 1:
            break
        sorted_li.append(tmp)
        new_li.remove(tmp)
    sorted_li.reverse()
    return sorted_li