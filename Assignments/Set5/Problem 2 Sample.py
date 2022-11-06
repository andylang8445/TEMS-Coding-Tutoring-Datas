from student_submit_S5P2 import decToBin
import random
import string

def decToBin_Ans(dec):
    if dec < 2:
        return str(dec)
    return decToBin_Ans(dec//2) + str((dec % 2))

def marking(correct_handeling: int):
    """
    Function for marking S5P2 student code with the file name student_submit_S5P2.py
        Args:
            correct_handeling: number of tests to run, recommended value is >100
        Returns:
            List[0]: correct hendeling result will be returned as index 0
            Note: The data will range between 0 - 100
    """
    
    correct_cnt = 0
    
    for _ in range(correct_handeling):
        num = random.randint(63, 1025)
        if decToBin_Ans(num) == decToBin(num):
            correct_cnt += 1
    return [(correct_cnt/correct_handeling) * 100]

print(marking(1024))