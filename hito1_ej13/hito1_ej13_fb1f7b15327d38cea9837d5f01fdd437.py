#Factores Primos
from os import system
system("cls")

def imprimir_factores_primos(numero):
        factor = 2
        while factor <= numero:
          if numero % factor == 0:
               print(factor)
               numero //= factor
          else:
               factor += 1
               numero = int(input())
               imprimir_factores_primos(numero)

