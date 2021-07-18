'''
https://www.acmicpc.net/problem/10814 
'''
l = [input().split() for i in range(int(input()))] # 첫 번째 줄 들어온 수만 큼 반복, 두 번째 줄 부터 들어오는 수와 이름을 배열에 저장
l.sort(key = lambda x : int(x[0])) # 배열을 각 이름의 첫 글자를 기준으로 정렬
for i in range(len(l)) :
    print(f'{l[i][0]} {l[i][1]}')