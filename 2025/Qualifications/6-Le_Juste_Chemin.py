from collections import deque


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 10**9 + 7

    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    scores = list(map(int, data[idx:idx+N]))
    idx += N
    
    routes = []
    for _ in range(M):
        A = int(data[idx])
        B = int(data[idx+1])
        routes.append((A-1, B-1))  # Convertir en indices
        idx += 2
    
    # Construire le graphe
    graph = [[] for _ in range(N)]
    for u, v in routes:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS pour calculer les distances depuis la maison 1 (index 0)
    distance = [float('inf')] * N
    distance[0] = 0
    queue = deque([0])
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distance[v] == float('inf'):
                distance[v] = distance[u] + 1
                queue.append(v)
    
    # Calculer la somme des scores des paires justes
    total = 0
    for u in range(N):
        for v in range(N):
            if distance[u] + distance[v] <= K:
                total = (total + scores[u] * scores[v]) % MOD
    
    print(total)

if __name__ == "__main__":
    main()