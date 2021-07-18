'''
https://www.acmicpc.net/problem/17211
'''
n, fd = map(int,input().split())
gg,gb,bg,bb = map(float,input().split())
good = [0 for i in range(n)]
bad = [0 for i in range(n)]
if fd == 0 :
    good[0] = gg
    bad[0] = gb
else :
    good[0] = bg
    bad[0] = bb
for i in range(1,n) :
    good[i] = good[i-1]*gg + bad[i-1]*bg
    bad[i] = good[i-1]*gb + bad[i-1]*bb
print(round(good[n-1]*1000))
print(round(bad[n-1]*1000))