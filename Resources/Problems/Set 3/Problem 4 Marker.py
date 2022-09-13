# Name the student submission python sile as Student_submit.py
# Run this code, then it will show the result.
# You can adjust the weights and number of testing
int_test = 10
int_test_weight = 10
double_test = 10
double_test_weight = 15
int_correct_count = 0
double_correct_count = 0
Mark = 0
Total_Mark = int_test_weight + double_test_weight

from Student_submit import p3SumTwoNum
import random
for i in range(int_test):
    a = random.randrange(1, 90000)
    b = random.randrange(1, 90000)
    student_Ans = p3SumTwoNum(a, b)
    if student_Ans == (a+b):
        int_correct_count += 1

for i in range(double_test):
    a = random.randrange(1, 90000)/100
    b = random.randrange(1, 90000)/100
    student_Ans = p3SumTwoNum(a, b)
    if student_Ans == (a+b):
        double_correct_count += 1

Mark = (int_correct_count/int_test)*int_test_weight
Mark += (double_correct_count/double_test)*double_test_weight

if int_correct_count == int_test:
    print("Integer Handeling Pass")
else:
    print("Integer Handeling Fail - Correct:",int_correct_count,"/",int_test)
if double_correct_count == double_test:
    print("Double Handeling Pass")
else:
    print("Double Handeling Fail - Correct:",double_correct_count,"/",double_test)

if Mark >= Total_Mark:
    print("All test Pass")
elif Mark > 0:
    print("Part Marks are given: ", Mark, "Out of ", Total_Mark)
else:
    print("No part marks are given")