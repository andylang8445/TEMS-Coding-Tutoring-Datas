import math
from student_submit_S5P3 import mySorting
import random

def mySorting_Ans(li: list):
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


def marking(correct_handeling: int):
    """
    Function for marking S5P3 student code with the file name student_submit_S5P3.py
        Args:
            correct_handeling: number of tests to run, recommended value is >100
        Returns:
            List[0]: correct hendeling result will be returned as index 0
            Note: The data will range between 0 - 100
    """
    
    correct_cnt = 0
    
    for _ in range(correct_handeling):
        li = []
        distance = [-1]
        length = random.randint(32, 128)
        i = [random.randint(0, 2048), random.randint(0, 2048)]
        li.append(i)
        distance.append(math.sqrt(((i[0] * i[0]) + (i[1] * i[1]))))
        for _ in range(length):
            tmp_distance = -1
            tmp = [0, 0]
            while tmp_distance in distance:
                tmp = [random.randint(0, 2048), random.randint(0, 2048)]
                tmp_distance = math.sqrt(((tmp[0] * tmp[0]) + (tmp[1] * tmp[1])))
            distance.append(tmp_distance)
            li.append(tmp)
        if mySorting(li) == mySorting_Ans(li):
            correct_cnt += 1
    return [(correct_cnt/correct_handeling) * 100]

print(marking(1024))