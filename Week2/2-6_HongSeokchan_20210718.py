'''
https://www.acmicpc.net/problem/1316 
'''
a = int(input())
ans=0
for i in range(a):
    word = input()
    for j in range(len(word)):
        if j!=len(word)-1:
            if word[j]==word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            ans+=1
print(ans)
