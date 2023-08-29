import random

secreto = random.randint(1,20)
adivinado = False
for i in range(0, 5):
    numero = int(input("Ingrese número: "))
    
    if numero == secreto:
        print("Adivinaste, mi número era", secreto)
        adivinado = True
        break
    elif numero > secreto:
        print("Mi número es menor")
    elif numero < secreto:
        print("Mi número es mayor")


if not adivinado:
    print("No adivinaste, mi número era", secreto,i)