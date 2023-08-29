def descomponer(n):
    primos = []

    for i in range(2, n + 1):
        while n % i == 0:
            primos.append(i)
            n = n / i  
    for i in range(len(primos)):
        print(primos[i])

x = int(input("Ingrese numero: "))
descomponer(x)