from random import randint

numeroParaAdivinar = randint(1,20)

intentos = 0
numeroAdivinado = 0

while intentos <= 5:
    if intentos > 1:
        numeroAdivinado = int(input("intenta de nuevo: "))
    else:
        numeroAdivinado = int(input("digita el numero que crees que tengo:"))
    intentos += 1
    if numeroAdivinado == numeroParaAdivinar:
        print("Adivinaste, mi número era", numeroParaAdivinar)
        break
    if numeroParaAdivinar > numeroAdivinado:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")
    if intentos == 5:
        print("No adivinaste, mi número era", numeroParaAdivinar)
        break