targetNum = 197
answerQ = 0
for i in range(5):
    tmp = int(input())
    if tmp > targetNum:
        print("Down")
    elif tmp == targetNum:
        print("Correct!")
        answerQ = 1
        break
    else:
        print("Up")
if answerQ == 0:
    print("Game Over: Answer was", targetNum)