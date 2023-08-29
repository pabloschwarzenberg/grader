import random
numeroIncognito = random.randint(1,20)
adivinaste = 0
for i in range(0,5):
    numero = int(input("Ingrese numero: "))
    if numero > numeroIncognito:
        print("Mi numero es menor")
    elif numero < numeroIncognito:
        print("Mi numero es mayor")
    else:
        adivinaste = 1
        print("Adivinaste, mi número era ", numeroIncognito)
        break
if adivinaste != 1:
    print("No adivinaste, mi número era ", numeroIncognito)
