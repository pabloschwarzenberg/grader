#Juego adivina mi número
import random
numero_secreto=random.randint(1,20)
cont=0
while True:
    numero=random.randint(1,20)
    cont+=1
    if numero==numero_secreto:
        print("Adivinaste, mi número era",numero_secreto)
        break
    elif numero<numero_secreto:
        print("mi número es mayor")
    elif numero>numero_secreto:
        print("mi número es menor")
    if cont==5:
        print("No adivinaste, mi número era",numero_secreto)
        break
