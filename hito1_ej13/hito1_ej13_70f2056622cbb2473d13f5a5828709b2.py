#Factores Primos
from os import system
system ("cls")

def descomposicion_primos(numero):
    i = 2
    while numero >= i:
        if numero % i == 0:
            print(i)
            numero = numero / i
    
        else:
            i += 1
    return
descomposicion_primos(int(input("Ingrese numero: ")))