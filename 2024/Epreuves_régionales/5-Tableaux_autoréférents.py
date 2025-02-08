N = int(input())
portes = list(map(int, input().split()))

def truc():
    for i in range(N):
        if portes.count(i) != portes[i]:
            return i
    return -1

print(truc())