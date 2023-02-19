from collections import deque

def getSLE(maps):
    S,L,E = 0,0,0
    for col, colValue in enumerate(maps):
        for row, rowValue in enumerate(maps[col]):
            if rowValue == 'S':
                S = (col,row)
            elif rowValue == 'L':
                L = (col,row)
            elif rowValue == 'E':
                E = (col, row)
                
    
    return S,L,E

def solution(maps):
    answer = 0
    lenCol = len(maps)
    lenRow = len(maps[0])
    S,L,E = getSLE(maps)
    
    def bfs(start, end):
        result = 0
        q = deque([(start[0], start[1], 0)])
        visited = {}

        while q:
            col, row, count = q.popleft()
            if (col, row) in visited:
                continue
            elif (col, row) == end:
                result = count
                break

            if col > 0 and maps[col-1][row] != 'X':
                q.append((col-1, row, count+1))
            if col < lenCol-1 and maps[col+1][row] != 'X':
                q.append((col+1, row, count+1))
            if row > 0 and maps[col][row-1] != 'X':
                q.append((col, row-1, count+1))
            if row < lenRow-1 and maps[col][row+1] != 'X':
                q.append((col, row+1, count+1))

            visited[(col, row)] = count
        
        if result == 0:
            return -1
        else:
            return result
    
    t = bfs(S, L)
    if t == -1:
        return -1
    answer += t
    
    t = bfs(L, E)
    if t == -1:
        return -1
    answer += t
    
    return answer