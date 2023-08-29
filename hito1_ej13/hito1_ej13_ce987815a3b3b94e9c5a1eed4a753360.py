#Factores Primos
def desc(n):
    primos = []
    for i in range(2,n+1):
        while n % i == 0:
            primos.append(i)
            n = n / i
    return primos
n = int(input("Ingresa un número: "))
respuesta = desc(n)
for valor in respuesta:
    print(valor)