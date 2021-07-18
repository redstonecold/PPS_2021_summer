'''
https://www.acmicpc.net/problem/2799 

접근 방식을 찾는데 어려움을 느껴 정답을 참고함
다시 풀어 볼 것
'''
zero = ["....", "....", "....", "...."]
one = ["****", "....", "....", "...."]
two = ["****", "****", "....", "...."]
three = ["****", "****", "****", "...."]
four = ["****", "****", "****", "****"]

M,N = map(int,input().split())
apt = []
while len(apt) < 5*M+1 :
    apt.append(input())

row, col = [], []
for m in range(M) :
    row.append(5*m+1)
for n in range(N) :
    col.append(5*n+1)

result = []
for r in row :
    for c in col :
        tmp = []
        tmp.append(apt[r][c:c+4])
        tmp.append(apt[r+1][c:c+4])
        tmp.append(apt[r+2][c:c+4])
        tmp.append(apt[r+3][c:c+4])
        result.append(tmp)

print(result.count(zero), result.count(one), result.count(two), result.count(three), result.count(four))