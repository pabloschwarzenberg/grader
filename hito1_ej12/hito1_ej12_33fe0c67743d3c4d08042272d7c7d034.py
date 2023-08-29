#Juego adivina mi número
## ENTRADA DE DATOS - PROCESO - SALIDA

import random

Número_secreto = random.randint(1, 20)
Intentos = 5

print("¡Bienvenido al Juego Adivina mi Número!")
print("He generado un Número Aleatorio entre 1 y 20,\nTienes 5 intentos para Adivinarlo.")

for i in range(Intentos):
    print("Intento", i + 1)
    Número_Jugador = int(input("Ingrese su Número: "))

    if Número_Jugador < Número_secreto:
        print("Mi Número es Mayor")
    elif Número_Jugador > Número_secreto:
        print("Mi Número es Menor")
    else:
        print("Adivinaste, mi Número era:", Número_secreto)
        break
else:
    print("No adivinaste, mi Número era:", Número_secreto)
    
      