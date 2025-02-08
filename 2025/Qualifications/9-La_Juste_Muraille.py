import itertools

def calculer_cout(sortie, entree, permutation):
    cout_total = 0
    n = len(permutation)
    for i in range(n):
        j = (i + 1) % n
        cout_total += (sortie[permutation[i]] - entree[permutation[j]]) ** 2
    return cout_total

def trouver_cycle_optimal(N, sortie, entree):
    tours = list(range(N))
    meilleur_cout = float('inf')
    meilleure_permutation = None
    
    for permutation in itertools.permutations(tours):
        cout = calculer_cout(sortie, entree, permutation)
        if cout < meilleur_cout:
            meilleur_cout = cout
            meilleure_permutation = permutation
    
    return meilleur_cout, meilleure_permutation

# Lecture de l'entrée
N = int(input())
sortie = list(map(int, input().split()))
entree = list(map(int, input().split()))

# Trouver le cycle optimal
cout, permutation = trouver_cycle_optimal(N, sortie, entree)

# Afficher le résultat
print(cout)
print(' '.join(map(str, permutation)) + ' ' + str(permutation[0]))