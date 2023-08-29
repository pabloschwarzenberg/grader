#Factores Primos
numero = int(input("Ingrese un numero: "))

def descomposicion(numero):
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            print(divisor)
            numero = numero / divisor
        else:
            divisor = divisor + 1

descomposicion(numero)
  