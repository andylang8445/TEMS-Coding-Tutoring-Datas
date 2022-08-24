# range: 0~200
n = int(input())
if n == 0:
    print(0)
elif n > 200:
    print("DNE")
else:
    for i in range(1, 201):
        if i % n == 0:
            print(i)