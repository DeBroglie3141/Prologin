
N = int(input())
M = int(input())
K = int(input())
scores = list(map(int, input().split()))
routes = [tuple(map(int, input().split())) for _ in range(M)]

print(N, M, K, scores, routes)
