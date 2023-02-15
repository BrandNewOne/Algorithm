import sys

K, P, N = map(int, sys.stdin.readline().split())

answer = 0
for i in range(N):
    K = ((K*P)%1000000007)

print(K)