N, M, l_M, l_M_faits, l_coeff = int(input()), int(input()), [], [], []
n = 0

for _ in range(N):
    l_M.append(str(input()))

for i in range(N):
    if l_M[i] not in l_M_faits :
        coeff = 1
        for j in range(i+1, N):
            if l_M[i] == l_M[j]:
                coeff += 1
        l_coeff.append(coeff)
        l_M_faits.append(l_M[i])

for t in l_coeff : 
    if int(t)%2 == 1 :
        n+= 1
        
print(n)