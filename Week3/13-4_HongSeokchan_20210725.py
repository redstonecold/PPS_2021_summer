import sys

input = sys.stdin.readline

n = int(input())
goaltmp = list(map(int,input().split()))

goal = []
for i in range(n):
  if goaltmp[i] == 0:
    goal.append(False)
  else : 
    goal.append(True)

now = [False for _ in range(n)]
ans = 0

for i in range(n):
  if now[i]!= goal[i]:
    now[i] = not now[i]

    if i + 1 < n :
      now[i+1] = not now[i+1]
      
    if i + 2 < n :
      now[i+2] = not now[i+2]
    ans = ans + 1

print(ans)