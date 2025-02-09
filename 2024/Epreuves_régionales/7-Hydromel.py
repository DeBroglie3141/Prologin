nbRecettes = int(input())
recettes = []

for  _ in range(nbRecettes):
    ethanol, coutMiel, limite = map(int, input().split())
    ratio = ethanol / coutMiel
    recettes.append((ratio, ethanol, coutMiel, limite))

qtitéMiel = int(input())

recettes.sort(reverse=True)

def hydromel(qtité_miel, qtité_ethanol, recettes):
    if (qtité_miel == 0) or not recettes:
        return qtité_ethanol
    _, ethanol, coutMiel, limite = map(int, recettes[0])
    nbLitres = min(qtité_miel/coutMiel, limite)
    qtité_ethanol += ethanol * nbLitres
    return hydromel(qtité_miel - nbLitres * coutMiel, qtité_ethanol, recettes[1:])

print(hydromel(qtitéMiel, 0, recettes))