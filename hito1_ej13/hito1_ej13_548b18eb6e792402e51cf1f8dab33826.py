def factores_primos(n):
    nprimos = []
    for i in range (2, n+1):
        while n % i == 0:
            nprimos.append(i)
            n = n/i
            print(nprimos)