'''def solution(skill, skill_trees):
    answer = -1

    for sk in skill_trees :
        index = 0
        for ch in sk :
            if skill.find(ch) == index : 
                index = index+1
                answer = answer + 1
            
    return answer'''

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        temp = 0
        for s in skill_tree:
            if s in skill:
                if skill.index(s) == temp: temp += 1
                else: break
        else: answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
answer = solution(skill, skill_trees)
print(answer)

'''
def solution(skill, skill_trees):
    answer = -1
    for sk in skill_trees :
        list1 = []
        for ch in skill :
            list1.append(sk.find(ch))
        list2 = sorted(list1)
        if list1 == list2 :
            if answer == -1 : answer = 0
            answer = answer + 1
        
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
answer = solution(skill, skill_trees)
print(answer)
'''