from itertools import combinations_with_replacement

def getScore(lionList, apeachList):
    lion = 0
    apeach = 0
    
    temp = [0,0,0,0,0,0,0,0,0,0,0]
    
    for l in lionList:
        temp[l] += 1
    
    temp.reverse()
    lionList = temp
    
    for i,(lionScore, apeachScore) in enumerate(zip(lionList, apeachList)):
        if lionScore == 0 and apeachScore == 0:
            continue
        elif lionScore > apeachScore:
            lion += (10-i)
        elif lionScore <= apeachScore:
            apeach += (10-i)
    
    if lion > apeach:
        return lion-apeach, lionList
    else:
        return -2 , [-1]
    

def solution(n, info):
    answer = [-1]
    s = -1
    score = [10,9,8,7,6,5,4,3,2,1,0]
    for lionInfo in combinations_with_replacement(score, n):
        tempScore, lion = getScore(lionInfo ,info)

        if tempScore > s:
            s = tempScore
            answer = lion
        elif tempScore == s:
            for i,j in zip(reversed(answer), reversed(lion)):
                if i == j:
                    continue
                if i < j:
                    answer = lion
                    break
                else:
                    break
                
    return answer
