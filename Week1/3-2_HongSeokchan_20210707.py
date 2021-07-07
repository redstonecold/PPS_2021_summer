'''
https://www.acmicpc.net/problem/11721
'''
s = input("")
for i in range((len(s)//10)+1) :
    print(s[10*i:10*(i+1)]) #매 일의자리 0~9까지 출력