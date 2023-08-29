#Factores Primos
# crear lista con primos

def factores_primos(numero):
    i = 2
    factores = []
    while i * i <= numero:
        if numero % i:
            i += 1
        else:
            numero //= i
            factores.append(i)
    if numero > 1:
        factores.append(numero)
    return factores


numero = int(input("ingresar numero: "))
factores = factores_primos(numero)

for x in factores:
    print(x)
      