N = int(input())
truc = list(map(int, input().split()))

somme_trous = 0
dans_un_trou = False
n = 0

truc.append(0)
# Parcours du tableau pour compter les trous
for i in range(1, N):
    if truc[i] == 0 and (truc[i - 1] == 1 or dans_un_trou):
        dans_un_trou = True
        n += 1
    elif truc[i] == 1 and dans_un_trou:
        dans_un_trou = False
        somme_trous += n
        n = 0

# Afficher le résultat
print(somme_trous)