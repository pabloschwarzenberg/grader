#Factores Primos
def descomposicion_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            print(factor)
            numero = numero / factor
        else:
            factor += 1

#Número para descomponer
numero = int(input("Ingrese un número entero: "))

#Descomposición
print("Descomposición de factores primos:")
descomposicion_factores_primos(numero)
