def primosd(n):
    primos = []
    for i in range(2, n+1):
        while n % i == 0:
            primos.append(i)
            n = n/i
    return primos
n=int(input())
resultado=(primosd(n))
for item in resultado:
    print(item)