N = int(input())
A = [input().strip() for _ in range(N)]
B = [input().strip() for _ in range(N)]
phrase = [a + b for a in A for b in B]
n_sup, n_inf = 0, 0

compte_mots = {}
for mot in phrase:
    if mot in compte_mots:
        compte_mots[mot] += 1
    else:
        compte_mots[mot] = 1

occurrences = list(compte_mots.values())

moyenne = sum(occurrences) / len(occurrences)
cible_inf = int(moyenne)
if moyenne != cible_inf :
    cible_sup = cible_inf + 1

for t in occurrences :
    n_inf += abs(t - cible_inf)
    n_sup += abs(t - cible_sup)

print(min(n_sup, n_inf))