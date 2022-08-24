sum = 0
tmp = ''
while True:
    tmp = input()
    if tmp == 'zzz':
        break
    sum += int(tmp)
print(sum)