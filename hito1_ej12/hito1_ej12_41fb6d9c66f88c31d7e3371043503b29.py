#Juego adivina mi número
import random
numero_magico=random.randint(1,20)
contador=5
while contador > 0:
    nro_jugador = int(input("Ingrese un número entre 1 y 20:"))
    if nro_jugador > numero_magico:
        print("mi número es menor")
    elif nro_jugador < numero_magico:
        print("mi número es mayor")
    elif nro_jugador == numero_magico:
        print("Adivinaste, mi número era",numero_magico)
        break
    contador=contador-1
