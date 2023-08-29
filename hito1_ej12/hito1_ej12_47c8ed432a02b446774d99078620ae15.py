#Juego adivina mi número

import random

numero_secreto = random.randint(1, 20)
intentos = 0

while intentos < 5:
    numero_usuario = int(input("Ingrese un número: "))
        
    if numero_secreto == numero_usuario:
            numero_secreto = str(numero_secreto)
            print("Adivinaste, mi número era "+numero_secreto)
            break
    elif numero_secreto < numero_usuario:
            print("Mi número es menor")
            intentos = intentos +1
    else:
                print("Mi número es mayor")

                intentos = intentos + 1
    
else:
    numero_secreto = str(numero_secreto)
    print("No adivinaste, mi número era "+numero_secreto)
