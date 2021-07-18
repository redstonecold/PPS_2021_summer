'''
https://www.acmicpc.net/problem/11866 
'''

from collections import deque

x,y = map(int,input().split())
d = deque([str(i) for i in range(1,x+1)])
ans = deque()
while len(d) > 0 :
    for i in range(y-1) :
        d.append(d.popleft())
    ans.append(d.popleft())
print("<",end="")
print(", ".join(list(ans)),end="")
print(">")