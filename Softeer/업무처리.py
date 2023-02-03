import sys
from collections import deque

def getHKR():
    H, K, R = map(int, sys.stdin.readline().split())
    return H, K, R


def getWorkList(H):
    workList = {}
    for i in range(2**H-1):
        workList[i] = deque([])

    for i in range(2**H):
        workList[2**H+i-1] = deque(list(map(int, sys.stdin.readline().split())))
    
    return workList

def solution():
    H, K, R = getHKR()
    workList = getWorkList(H)

    if R <= H:
        return 0
    
    answer = 0
    
    for day in range(R-1):
        for worker, work in list(workList.items()):
            if day%2 == 1:
                childWorker = (worker+1)*2-1
            else:
                childWorker = (worker+1)*2
            
            if childWorker not in workList:
                continue
            if workList[childWorker]:
                workList[worker].append(workList[childWorker].popleft())
            

    return sum(workList[0])

print(solution())