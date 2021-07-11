'''
https://programmers.co.kr/learn/courses/30/lessons/49993
'''
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees :
        temp = 0
        for s in skill_tree :
            if s in skill :
                if skill.index(s) == temp :
                    temp += 1
                else : break
        else : answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
answer = solution(skill, skill_trees)
print(answer)
