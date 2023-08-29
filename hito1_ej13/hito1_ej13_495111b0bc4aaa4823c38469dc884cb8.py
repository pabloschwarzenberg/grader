#Factores Primos
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False

    limite = int(round(numero**(1/2)))

    i = 3
    while i <= limite:
        if numero % i == 0:
            return False
        i = i + 3

    return True

# Inicio de programa #
num = int(input("Ingrese un numero para sacar sus factores primos: "))
primos = []

for x in range(num+1):
    if es_primo(x):
        primos.append(x)

fac_prim = []
n = 0

while num > 1:
    for y in primos:
        if num % y == 0:
            fac_prim.append(y)
            num = num / fac_prim[0 + n]
            n = n + 1

for z in fac_prim:
    print(z)
      