from os import system
system("cls")

def es_primo(numero):
     if numero < 2:  # Los números menores a 2 no son primos
          return False
     for i in range(2, int(numero ** 0.5) + 1):
         if numero % i == 0:  # Si el número es divisible por otro número, no es primo
             return False
         return True

numero = int(input("Ingrese un número: "))
if es_primo(numero): print("Es primo")
else:
    print("No es primo")