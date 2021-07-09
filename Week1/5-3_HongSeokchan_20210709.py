'''
programmers 탐욕법 > 큰 수 구하기
https://programmers.co.kr/learn/courses/30/lessons/42883

정말 어려웠던 문제, 스택 개념 사용, 구글링 도움 받은 후 이해
'''
def solution(number, k):
    answer = []
    for num in number :
        while answer and k > 0 and num > answer[-1]: #answer을 먼저 씀으로써 처음에 answer[-1]에서 indexing 문제가 나는 것을 막을 수 있음
            answer.pop(-1)
            k -= 1
        answer.append(num)
    return "".join(answer[:len(answer) - k]) # 이걸 왜 이렇게 써야만 할까? 결국 같은거 같은데..?

number = "4177252841"
k = 4
print(solution(number,k))