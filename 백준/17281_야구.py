import sys
from itertools import permutations

N = int(sys.stdin.readline().strip())

answer = 0
perm = permutations([1,2,3,4,5,6,7,8], 8)

inning = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    inning.append(temp)


for p in perm:
    tempAnswer = 0
    now = 0
    
    for i in inning:
        tempInning = [i[p[0]],i[p[1]],i[p[2]],i[0],i[p[3]],i[p[4]],i[p[5]],i[p[6]],i[p[7]]]
        outCount = 0
        base1, base2, base3 = 0,0,0
        while outCount < 3:
            if tempInning[now] == 0:
                outCount += 1
            elif tempInning[now] == 1:
                tempAnswer += base3
                base1, base2, base3 = 1, base1, base2
            elif tempInning[now] == 2:
                tempAnswer += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif tempInning[now] == 3:
                tempAnswer += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            else:
                tempAnswer += (base1 + base2 + base3+1)
                base1, base2, base3 = 0,0,0
                
            now = (now+1)%9
    
    answer = max(answer, tempAnswer)
    
print(answer)
    
    
            
    