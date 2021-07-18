'''
https://programmers.co.kr/learn/courses/30/lessons/12977 
'''
from itertools import combinations
from math import sqrt

def solution(nums):
    answer = []
    pnums = list(map(sum, combinations(nums,3)))
    print(pnums)
    for n in pnums :
        if n > 1:
            for i in range(2,int(sqrt(n))+1) :
                if n%i == 0 : break
            else : answer.append(n)
    return len(answer)

nums = [1,2,3,4]
print(solution(nums))