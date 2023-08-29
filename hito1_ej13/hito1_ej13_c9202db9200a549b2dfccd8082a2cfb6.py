#Factores Primos
def descomponer(n):

    nprimos = []

    for i in range(2,n+1):
        while n%i == 0:
            nprimos.append(i)
            n = n / i
    return nprimos

n = int(input('Ingrese un número: '))

a = descomponer(n)

for i in a:
    print(i)