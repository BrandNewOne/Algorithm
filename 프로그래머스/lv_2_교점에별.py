def meet(A,B,E,C,D,F):
    x = (B*F - E*D)/(A*D - B*C)
    y = (E*C - A*F)/(A*D - B*C)
    
    return x, y

def solution(line):
    meetList = set()
    for i,(A,B,E) in enumerate(line):
        for j,(C,D,F) in enumerate(line[i+1:]):
            if A*D-B*C != 0:
                x, y = meet(A,B,E,C,D,F)
                if x == int(x) and y == int(y):
                    meetList.add(meet(A,B,E,C,D,F))
    
    minX, minY = 1000000000000000, 1000000000000000
    maxX, maxY = -1000000000000000, -1000000000000000
    for x,y in meetList:
        if x < minX: minX = int(x)
        if x > maxX: maxX = int(x)
        if y < minY: minY = int(y)
        if y > maxY: maxY = int(y)
           
    board = []
    row = abs(maxX-minX)
    col = abs(maxY-minY)
    
    #print(meetList, minX, minY)
    for i in range(col+1):
        y = i+minY
        tempRow = ''
        for j in range(row+1):
            x = j+minX
            if (x, y) in meetList:
                tempRow += '*'
            else:
                tempRow+='.'
        
        board.append(tempRow)
        
    board.reverse()
    return board