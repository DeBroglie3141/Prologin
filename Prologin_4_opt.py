N = int(input())
valeur = int(input())
boites = list(map(int, input().split()))

somme_cumulative = 0
restes = {0: 1} 
n = 0

for boite in boites:
    somme_cumulative += boite
    reste = somme_cumulative % valeur
    
    if reste < 0:
        reste += valeur
    
    if reste in restes:
        n += restes[reste]
        restes[reste] += 1
    else:
        restes[reste] = 1

print(n % 1000000007)
