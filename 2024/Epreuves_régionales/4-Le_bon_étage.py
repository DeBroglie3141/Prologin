N = int(input())
liste = list(map(int, input().split()))
def truc():
    i = 0
    while liste[i] != i:
        i = liste[i]
    return i
print(truc())