dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

str = input()

sum = 0
for ch in str :
    num = 3
    for alphabet in dial :
        if ch in alphabet :
            sum = sum+num
        num = num+1
print(sum)