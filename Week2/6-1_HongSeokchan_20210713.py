'''
https://www.acmicpc.net/problem/2164 
'''
from collections import deque

deq = deque(list(range(1, int(input())+1))) # 1~N 까지의 숫자가 담긴 deque
while len(deq) > 1 : # 카드가 한 장 남을 때까지
    deq.popleft() # 제일 위에 있는 카드 버리기
    deq.append(deq.popleft()) # 제일 위에 있는 카드를 제일 아래로 내리기
print(deq.popleft())


'''
s = "".join([str(x) for x in range(1,int(input())+1)])
ls = len(s)
while ls > 1 : s = s[2:ls]+s[1]
print(s)
'''


