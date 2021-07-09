'''
https://www.acmicpc.net/problem/3052
'''
setnum = set()

for i in range(10) :
    num = int(input())%42
    setnum.add(num)
print(len(setnum))