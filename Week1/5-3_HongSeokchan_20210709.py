import copy
def solution(number, k):
    snum = sorted(copy.deepcopy(number))
    print(snum)
    for i in range(k) :
        print(snum[i])
        number = number.replace(snum[i],"",1)
    return number

number = "1231234"
k = 3
print(solution(number,k))