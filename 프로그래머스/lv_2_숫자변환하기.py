from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    q = deque([(x+n,1), (x*2,1), (x*3,1)])
    arr = [-1 for i in range(y+1)]
    
    while q:
        v,cnt = q.popleft()
        #print(v,cnt)
        
        if v < y:
            if v+n <= y and arr[v+n] == -1:
                q.append((v+n, cnt+1))
                arr[v+n] = cnt+1
            if v*2 <= y and arr[v*2] == -1:
                q.append((v*2, cnt+1))
                arr[v*2] = cnt+1
            if v*3 <= y and arr[v*3] == -1:
                q.append((v*3, cnt+1))
                arr[v*3] = cnt+1
        elif v == y:
            arr[v] = cnt
            break
    
    return arr[y]

print(solution(10,40,5)) # 2
print(solution(10,40,30)) # 1
print(solution(2,5,4)) # -1
print(solution(2,13,1)) # 3
print(solution(2,14,1)) # 3
print(solution(2,15,1)) # 3