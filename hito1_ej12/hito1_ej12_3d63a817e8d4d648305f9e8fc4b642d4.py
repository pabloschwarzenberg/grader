#Juego adivina mi número
#importaciones
import random

#entrada
n_secreto = random.randint(1,20)

i=0
n_jugada=0
while i < 5 and n_secreto != n_jugada:
    print("INTENTO ", i+1)
    n_jugada = int(input("ingrese su número entre 1 y 20: "))
    if n_secreto < n_jugada:
        print("mi número es mayor")
        i+=1
    elif n_secreto > n_jugada:
        print("mi número es menor")
        i+=1
    elif n_secreto == n_jugada:
        print("Adivinaste, mi número era ", n_secreto)