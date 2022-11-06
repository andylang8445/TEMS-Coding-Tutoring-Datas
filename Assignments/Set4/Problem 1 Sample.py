variable = input()
li = []
sub = ""
for i in variable:
    if i == ":":
        li.append(sub)
        sub = ""
    else:
        sub += i
if sub != "":
    li.append(sub)
for i in li:
    print(i)