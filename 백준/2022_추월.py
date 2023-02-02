import sys
from collections import deque

def inputData():
    n = int(sys.stdin.readline().strip())

    inArea = deque([])
    outArea = deque([])

    for i in range(n):
        s = sys.stdin.readline().strip()
        inArea.append(s)
        
    for i in range(n):
        s = sys.stdin.readline().strip()
        outArea.append(s)
    return inArea, outArea

def solution():
    answer = 0
    inArea, outArea = inputData()
    passed = set()    
    while outArea:
        if outArea[0] == inArea[0]:
            outArea.popleft()
            inArea.popleft()
        else:
            if inArea[0] in passed:
                inArea.popleft()
            else:
                answer+=1
                passed.add(outArea.popleft())
                
    
    return answer


print(solution())