from collections import defaultdict

motif, seuil, N = input(), int(input()), int(input())
len_motif = len(motif)
dico = {}

for _ in range(N):
    phrase = input()
    erreurs = 0
    for i in range(len_motif):
        if erreurs < seuil:
            if motif[i] != phrase[i]:
                erreurs += 1
        else:
            pass
    dico[erreurs] += (phrase)

if not dico:
    print('Aucune phrase valide')
else:
    for key in dico.keys():
        print(*dico[key], sep="\n")