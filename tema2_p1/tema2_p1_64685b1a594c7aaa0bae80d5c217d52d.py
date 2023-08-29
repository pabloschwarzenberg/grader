# por favor escribe aquí tu función
def descomponer(n):
    es_primo = []

    for i in range(2, n+1):
        while n % i == 0:
            es_primo.append(i)
            n = n / i
        return es_primo

print(descomponer(22))