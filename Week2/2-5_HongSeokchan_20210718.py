'''
https://www.acmicpc.net/problem/1157
'''
d = {}
for ch in input().upper() :
    if ch not in d :
        d[ch] = 0
    d[ch] += 1
val = sorted(d.values(),reverse=True)
if len(val) != 1 and val[0] == val[1] :
    print("?")
else :
    print(next(k for k, v in d.items() if v is val[0]))
