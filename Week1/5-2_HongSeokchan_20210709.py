'''
https://www.acmicpc.net/problem/5355 
'''

dic = dict(zip(['@', '%', '#'],["*3","+5","-7"]))

for i in range(int(input())) :
    eq = input().split()
    for j in range(1,len(eq)) :
        eq[0] = str(eval(eq[0]+dic[eq[j]]))
    print("%.2f"%float(eq[0]))