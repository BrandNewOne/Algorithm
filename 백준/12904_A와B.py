import sys
from collections import deque

S = deque(list(sys.stdin.readline().strip()))
T = deque(list(sys.stdin.readline().strip()))

def solution():
    peek = len(T)-1
    
    for i in range(len(T) - len(S)):
        if peek == 0:
            v = T.popleft()
            if v == 'B':
                peek = len(T)-1
        else:
            v = T.pop()
            if v == 'B':
                peek = 0


    if peek == 0:
        S.reverse()
    if S == T:
        return 1
    else:
        return 0

print(solution())