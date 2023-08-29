#Juego adivina mi número
import random

numero_mio=random.randint(1,20)
intentos=5
adivinar=False


while intentos>0:
    numero_pc=int(input())
    if numero_mio!=numero_pc:
        if numero_mio>numero_pc:
            print("MAYOR")
        else:
            print("MENOR")
        intentos=intentos-1

    else:
        adivinar=True
        print("Adivinaste, mi numero era",numero_mio)
        break
    
if not adivinar:
    print("No adivinaste, mi numero era", numero_mio)