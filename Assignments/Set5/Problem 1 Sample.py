from student_submit_S5P1 import isPalindrome
import random
import string

def isPalindrome_Ans(s):
    print(s, len(s), s[1:len(s)-1])
    if len(s) == 1 or len(s) == 0:
        return 1
    if s[0] != s[len(s)-1]:
        return 0
    return isPalindrome_Ans(s[1:len(s)-1])

def marking(correct_handeling: int, wrong_handeling: int):
    """
    Function for marking S5P1 student code with the file name student_submit_S5P1.py
        Args:
            correct_handeling: number of tests to run for correct info handelling
            wrong_handeling: number of tests to run for wrong info handelling
        Returns:
            List[0]: correct hendeling result will be returned as index 0
            List[1]: wrong handeling result will be returned as index 1
            Note: The data will range between 0 - 100
    """
    
    correct_cnt = 0
    wrong_cnt = 0
    
    for i in range(correct_handeling):
        length = random.randint(5, 34)
        word = ""
        if length % 2 != 0:
            length -= 1
            word = list(string.ascii_lowercase)[random.randint(0, 25)]
        for j in range(length//2):
            tmp = list(string.ascii_lowercase)[random.randint(0, 25)]
            word = tmp + word + tmp
        if isPalindrome(word) == 1:
            correct_cnt += 1

    for i in range(wrong_handeling):
        length = random.randint(5, 34)
        word = ""
        if length % 2 != 0:
            length -= 1
            word = list(string.ascii_lowercase)[random.randint(0, 25)]
        for j in range(length//2):
            tmp1 = ""
            tmp2 = ""
            while tmp1 == tmp2:
                tmp1 = list(string.ascii_lowercase)[random.randint(0, 25)]
                tmp2 = list(string.ascii_lowercase)[random.randint(0, 25)]
            word = tmp1 + word + tmp2
        if isPalindrome(word) == 0:
            wrong_cnt += 1
    return [(correct_cnt/correct_handeling) * 100, (wrong_cnt/wrong_handeling)*100]

print(marking(15, 15))