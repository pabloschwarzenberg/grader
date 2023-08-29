#Factores Primos
numero = int(input())
def es_primo_1(num):
    if num <2:
        return False
    for k in range(2, num):
        if num %k ==0:
            return False
    return True
   
def obtenerFactores(numero):
    factores = []
    for n in range(1,numero +1):
        if numero%n == 0:
            factores.append(n)
    return factores
   
factores = obtenerFactores(numero)
if len(factores) == 2:
    print(factores[1])
else:
    factores.pop(0)
    factores.pop(len(factores) - 1)
    print(factores)
    for f in factores:
        esPrimo = es_primo_1(f)
        if(esPrimo):
            print(f)