N = int(input())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

dico = {}
dico_A, dico_B = {}, {}

for a in A:
    if a in dico_A :
        dico_A[a] += 1
    else:
        dico_A[a] = 1

for b in B:
    if b in dico_B :
        dico_B[b] += 1
    else:
        dico_B[b] = 1

for a in dico_A:
    for b in dico_B:
        mot = a + b
        if mot in dico :
            dico[mot] += dico_A[a]*dico_B[b]
        else:
            dico[mot] = dico_A[a]*dico_B[b]

liste = sorted([dico[mot] for mot in dico])
longueur = len(liste)

somme = liste[0]
somme_cumul = [somme]
for i in range(1, longueur):
    somme += liste[i]
    somme_cumul.append(somme)
somme_total = somme_cumul[-1]

dico_index = {}
for i in range(longueur-1, -1, -1):
    if liste[i] not in dico_index:
        dico_index[liste[i]] = i

valeur_teste = set()
nombre_modiff_min = somme_total
moyenne_min = 0
last_smallest = -1
liste_temps = []
for i, moyenne in enumerate(liste):
    if moyenne not in valeur_teste:
        valeur_teste.add(moyenne)
        demi_moyenne = moyenne // 2
        while (last_smallest + 1 < longueur) and (liste[last_smallest + 1] <= demi_moyenne):
            last_smallest += 1
        if last_smallest != -1:
            index = dico_index[liste[last_smallest]]
            nombre_modiff = somme_cumul[index]
            nombre_modiff += moyenne*(i - index) - (somme_cumul[i] - somme_cumul[index])
            nombre_modiff += (somme_total - somme_cumul[i]) - moyenne*(longueur - i - 1)
        else:
            nombre_modiff = moyenne*(i + 1) - somme_cumul[i]
            nombre_modiff += (somme_total - somme_cumul[i]) - moyenne*(longueur - i - 1)

        if nombre_modiff < nombre_modiff_min:
            nombre_modiff_min = nombre_modiff
            moyenne_min = moyenne

print(nombre_modiff_min)