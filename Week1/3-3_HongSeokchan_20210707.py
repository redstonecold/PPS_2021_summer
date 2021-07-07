'''
https://www.acmicpc.net/problem/5598
'''

org = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
kai = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

dic = {}
for i in range(len(org)) :
    dic[kai[i]] = org[i] # dictionary 생성

s = input()
o = ''
for ch in s :
    o = o + dic[ch] #문자 치환 후 output string에 붙여줌
print(o)