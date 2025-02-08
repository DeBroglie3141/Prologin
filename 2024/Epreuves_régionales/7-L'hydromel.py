print('hello')

nbRecettes = int(input())
recettes = [input().split() for _ in range(nbRecettes)]
print(*recettes, sep='\n')