'''
https://www.acmicpc.net/status?user_id=hsch01&problem_id=1159&from_mine=1 
'''
sc = {}
x = int(input())

for i in range(x) :
    f = input()[0]
    if f not in sc.keys() :
        sc[f] = 0
    sc[f] += 1
ans = []

for i in sc.keys() :
    if sc[i] >= 5 :
        ans.append(i)

if len(ans) == 0 :
    print("PREDAJA")
else :
    ans.sort()
    print("".join(ans))