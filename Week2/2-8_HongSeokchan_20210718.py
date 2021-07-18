alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXZ'
ilist = [input() for x in range(int(input()))]
i = 0
for s in ilist :
    i+=1 
    print(f"String #{i}")
    for j in range(len(s)) :
        if s[j] == 'Z' : s = s.replace(s[j],'A')
        else : s = s.replace(s[j],alpha[alpha.find(s[j])+1])
    print(s)
