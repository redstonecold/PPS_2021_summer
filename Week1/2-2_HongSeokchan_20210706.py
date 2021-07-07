testnum = int(input())

for i in range(testnum) :
    ac = 1
    sum = 0
    answer = input()
    for ox in answer :
        if ox == 'O' :
            sum = sum + ac
            ac = ac + 1
        elif ox == 'X' :
            ac = 1
    print(sum)