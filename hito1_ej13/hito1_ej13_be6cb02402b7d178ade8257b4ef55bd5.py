#Factores Primos
def descomposicion(numero):
    factores_primos = []
    for i in range(2, numero+1):
        while numero % i == 0:
            factores_primos.append(i)
            numero = (numero / i)
    return factores_primos
    
numero = int(input("Ingrese un numero: "))
resultado = descomposicion(numero)

for i in resultado:
    print(i)