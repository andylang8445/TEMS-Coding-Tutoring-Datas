db = input().split(' ')
tmp = ''
while True:
    tmp = input()
    if tmp == '-1':
        break
    flag = 0
    for i in db:
        if i == tmp:
            print('exists')
            flag = 1
            break
    if flag == 0:
        print("DNE")