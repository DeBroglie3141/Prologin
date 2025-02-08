motif, seuil, N = input(), int(input()), int(input())
len_motif = len(motif)
phrases_correctes = []

for _ in range(N):
    phrase = input()
    erreurs = 0
    for i in range(len_motif):
        if motif[i] != phrase[i]:
            erreurs += 1
    if erreurs <= seuil:
        phrases_correctes.append((erreurs, phrase))

if not phrases_correctes:
    print('Aucune phrase valide')
else:
    phrases_correctes.sort()
    for _, phrase in phrases_correctes:
        print(phrase)