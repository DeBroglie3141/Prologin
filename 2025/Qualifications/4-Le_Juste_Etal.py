N, valeur, boites = int(input()), int(input()), list(str(input()).split(' '))
n = 0
for i in range(N):
    for j in range(i+1, N+1):
        somme = sum(int(boites[k]) for k in range(i,j))
        if somme%valeur == 0 :
            n += 1
        

print(n%1000000007)

