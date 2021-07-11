'''
https://www.acmicpc.net/problem/17210 
'''

dnum = int(input(""))
fway = int(input(""))
way = []

if dnum >= 6 : print("Love is open door")
else :
    for i in range(2,dnum+1) :
        if fway == 0 :
            if i%2 == 0 : way.append(1)
            else : way.append(0)
        else :
            if i%2 == 0 : way.append(0)
            else : way.append(1)
    for w in way : print(w)