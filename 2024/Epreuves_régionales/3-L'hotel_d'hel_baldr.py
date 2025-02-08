N = int(input())
n = 0

while N > 1:
    if N%3==0:
        N /= 3
    elif N%2==0:
        N /= 2
    else:
        N = 5*N + 1
    n += 1

print(n)