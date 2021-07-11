'''
https://www.acmicpc.net/problem/2775 
'''
ans = []
a = int(input())
for i in range(a) :
    ch = int(input())
    ho = int(input())
    p = [int(x) for x in range(1,ho+1)]
    for i in range (ch) :
        for j in range (1,ho) :
            p[j] += p[j-1]
    ans.append(p[-1])
for an in ans :
    print(an)