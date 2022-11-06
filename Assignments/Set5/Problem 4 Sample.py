import math
from student_submit_S5P4 import roomAssignment
import random

def roomAssignment_Ans(schedule:list):
    schedule.sort(key = lambda x: (x[1], x[0])) # sort based on ending time, and if the ending time is the same, sort by start time

    cnt = 0
    end = 0
    val = []
    for meeting in schedule:
        if meeting[0] >= end:
            cnt += 1
            val.append(meeting)
            end = meeting[1]
    print(val)
    return cnt



def marking(correct_handeling: int):
    """
    Function for marking S5P4 student code with the file name student_submit_S5P4.py
        Args:
            correct_handeling: number of tests to run, recommended value is >100
        Returns:
            List[0]: correct hendeling result will be returned as index 0
            Note: The data will range between 0 - 100
    """
    
    correct_cnt = 0
    
    for _ in range(correct_handeling):
        length = random.randint(11, 1000)
        schedule = []
        for _ in range(length):
            start = random.randint(0, 1000)
            end = random.randint(start, 2000)
            schedule.append([start, end])
        if roomAssignment(schedule) == roomAssignment_Ans(schedule):
            correct_cnt += 1
    return [(correct_cnt/correct_handeling) * 100]

#print(marking(1024))
print(roomAssignment_Ans([[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10],[8, 11], [8, 12], [2, 13], [12, 14]]))
print(roomAssignment_Ans([[326, 681], [621, 915], [992, 1747], [48, 1278], [912, 1048], [489, 1117], [338, 1218], [812, 825], [969, 1713], [481, 916]]))
print(roomAssignment_Ans([[19, 40], [10, 39], [10, 63], [24, 45], [12, 33], [19, 53], [22, 52], [18, 39], [16, 63], [1, 30]]))