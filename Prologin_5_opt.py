N = int(input())
A = [input().strip() for _ in range(N)]
B = [input().strip() for _ in range(N)]
phrase = [a + b for a in A for b in B]
liste_min = []

compte_mots = {}
for mot in phrase:
    if mot in compte_mots:
        compte_mots[mot] += 1
    else:
        compte_mots[mot] = 1

occurrences = list(compte_mots.values())
occurrences.sort()

def calcul():
    n_inf_beta, n_sup_beta = 0, 0
    moyenne = sum(occurrences) / len(occurrences)
    cible_inf = int(moyenne)
    cible_sup = cible_inf + 1

    for t in occurrences :
        n_inf_beta += abs(t - cible_inf)
        n_sup_beta += abs(t - cible_sup)

    return min(n_sup_beta, n_inf_beta)

liste_min.append(calcul())

for i in range(len(occurrences)):
    liste_min.append(calcul()+i+1)
    #print(liste_min)
    occurrences.pop(0)


print(min(liste_min))