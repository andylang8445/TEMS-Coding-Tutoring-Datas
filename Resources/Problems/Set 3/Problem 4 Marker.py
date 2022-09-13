# Name the student submission python sile as Student_submit.py
# Run this code, then it will show the result.
# You can adjust the weights and number of testing
int_test = 10
int_test_weight = 10
duplicate_test = 10
duplicate_test_weight = 15
int_correct_count = 0
duplicate_correct_count = 0
list_length_between = (20, 100)
Mark = 0
Total_Mark = int_test_weight + duplicate_test_weight

from Student_submit import searcher
import random
for i in range(int_test):
    li = list()
    for j in range(random.randrange(list_length_between[0], list_length_between[1])):
        tmp = random.randrange(-90000, 90000)
        if tmp not in li:
            li.append(tmp)
    li.sort()
    data = li[random.randrange(0, len(li))]
    student_Ans = searcher(li, data)
    print("Original list: ", li,", Looking for ", data)
    print("\tIndex: ", student_Ans, ", pointing at ", li[student_Ans])
    if li[student_Ans] == data:
        int_correct_count += 1
print("===================")
for i in range(duplicate_test):
    li = []
    for j in range(random.randrange(list_length_between[0], list_length_between[1])):
        tmp = random.randrange(-90000, 90000)
        li.append(tmp)
    li.sort()
    data = li[random.randrange(0, len(li))]
    student_Ans = searcher(li, data)
    print("Original list: ", li,", Looking for ", data)
    print("\tIndex: ", student_Ans, ", pointing at ", li[student_Ans])
    if li[student_Ans] == data:
        duplicate_correct_count += 1

Mark = (int_correct_count/int_test)*int_test_weight
Mark += (duplicate_correct_count/duplicate_test)*duplicate_test_weight

if int_correct_count == int_test:
    print("Integer Handeling Pass")
else:
    print("Integer Handeling Fail - Correct:",int_correct_count,"/",int_test)
if duplicate_correct_count == duplicate_test:
    print("Duplicate Handeling Pass")
else:
    print("Duplicate Handeling Fail - Correct:",duplicate_correct_count,"/",duplicate_test)

if Mark >= Total_Mark:
    print("All test Pass")
elif Mark > 0:
    print("Part Marks are given: ", Mark, "Out of ", Total_Mark)
else:
    print("No part marks are given")