vowelList = ['a', 'e', 'i', 'o', 'u']
ans = []

while True : 
    password = input() 
    if password == 'end' : break #end일 시 break
    
    checkVOWEL = False
    continuity = 0
    preword = ''
    proper = True

    for word in password : #문자열에서 한 문자씩 비교
        if word == preword and word+preword != 'ee' and word+preword != 'oo' : proper = False #같은 글자가 연속적으로 두번 오면 proper=false (ee 와 oo는 제외).
        if word in vowelList : #해당 문자가 모음일 때
            checkVOWEL = True 
            if preword in vowelList : #이전 문자가 모음이면 continuity + 1
                continuity = continuity + 1
            else : continuity = 0 #자음이면 continuity = 0
        else : #해당 문자가 자음일 때
            if preword not in vowelList : #이전 문자가 자음이면 continuity + 1
                continuity = continuity + 1
            else : continuity = 0 #모음이면 continuity = 0
        preword = word #다음 문자로 넘어가기전 현재 문자를 이전 문자로 설정
        if continuity > 1 : proper = False #같은 문자가 3번 이상 나오면 proper = False

    if checkVOWEL == False : proper = False #모음이 없었으면 proper = False

    if proper :
        ans.append("<%s> is acceptable."%password)
    else :
        ans.append("<%s> is not acceptable."%password)

for str in ans :
    print(str)
    
'''
l = "aeiou"
while True:
    s = input()
    chk,chk2 = 0,0
    if s == "end": break;
    for i in s:
        if i in l:
            chk2=1
    #print(chk2)
    for i in range(1,len(s)):
        if s[i] == s[i-1] and s[i] not in 'eo': chk=1
    #print(chk)
    for i in range(len(s)-2):
        if s[i] in l and s[i+1] in l and s[i+2] in l: chk=1
        elif s[i] not in l and s[i+1] not in l and s[i+2] not in l: chk=1
    #print(chk)
    if chk == 1 or chk2 == 0: print("<" + s + "> is not acceptable." )
    else: print("<" + s + "> is acceptable." 
'''