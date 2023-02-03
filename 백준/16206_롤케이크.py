import sys

def getM():
    N, M = map(int, sys.stdin.readline().split())
    
    return M

def getCakes():
    cakes = list(map(int, sys.stdin.readline().split()))
    cakes.sort()

    return cakes

def solution():
    answer = 0
    passed = 0
    M = getM()
    cakes = getCakes()
    
    for cake in cakes:
        if cake == 10:
            answer += 1
        elif cake%10 == 0:
            canDiv = cake//10

            if M-(canDiv-1) >= 0:
                answer += canDiv
                M -= (canDiv-1)
            else:
                answer += M
                M = 0
                break
                
        else:
            passed += cake//10

    if M > passed:
        answer += passed
    else:
        answer += M
        
    return answer

print(solution())