longueur, tunnel = int(input()), list(str(input()).split(' '))
liste_nb_0, liste_nb_1 = [], []
nb_0, nb_1 = 0, 0

for tunnel_i in tunnel:
    if tunnel_i == '1':
        if nb_0 != 0 :
            liste_nb_0.append(nb_0)
            nb_0 = 0
        nb_1 += 1
    else :
        liste_nb_1.append(nb_1)
        nb_0 += 1
        nb_1 = 0

if nb_0 != 0 :
    liste_nb_0.append(nb_0)
liste_nb_1.append(nb_1)

R, E = min(liste_nb_0), max(liste_nb_1)
print(R - E)