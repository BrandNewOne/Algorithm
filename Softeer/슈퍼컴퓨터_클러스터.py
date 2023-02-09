import sys

def getComputers():
    coms = list(map(int, sys.stdin.readline().split()))
        
    computers = {}
    for com in coms:
        if com in computers:
            computers[com] += 1
        else:
            computers[com] = 1
    
    return computers

N, B = map(int, sys.stdin.readline().split())
computersDict = getComputers()
computersList = sorted([k for k in computersDict.keys()])

def getPrice(v):
    return sum([computersDict[com] * ((v-com)**2) for com in computersList if com < v])

def getresult(start, end):
    visited = set()
    node = (start + end)//2
    result = start
    while start != node:
        visited.add(node)
        price = getPrice(node)
        if price < B:
            start = node
            result = node
        elif price > B:
            end = node
        else:
            result = node
            break
        
        node = (start + end)//2
        
    return result
            
def solution():
    answer = 0
    
    end = 1000000000000000000
    start = 1
    answer = getresult(start, end)

    return answer



print(solution())

