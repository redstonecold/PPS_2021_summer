testcase = int(input())

ans = []
for j in range(testcase) :
    inputlist = input().split()
    for i in range(len(inputlist)) :
        inputlist[i] = int(inputlist[i])
    # print(inputlist)

    sum = 0
    for i in range(1,inputlist[0]+1) :
        sum = sum + inputlist[i]
    avg = sum / inputlist[0]

    abavg = 0
    for i in range(1,inputlist[0]+1) :
        if inputlist[i] > avg :
            abavg = abavg + 1

    prc = abavg/inputlist[0] * 100
    ans.append(prc)

for j in ans :
    print("%.3f"%j,end='')
    print('%')