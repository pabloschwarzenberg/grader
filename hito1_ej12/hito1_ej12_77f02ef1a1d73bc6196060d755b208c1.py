import random
numeroSecreto = random.randint(0, 20)
numeroAdivinado = ""
intentos = 0
maxIntentos = 5
haAdivinado = False

print("Adivina el numero secreto")
while not haAdivinado and intentos < maxIntentos:
    num = int(input("Ingresa el numero: "))
    if int(num) < numeroSecreto:
        print("Mi numero es mayor")
        intentos += 1
    elif int(num) > numeroSecreto:
        print("Mi numero es menor")
        intentos += 1
    elif num == numeroSecreto:
        haAdivinado = True
if haAdivinado:
    print("Adivinaste, el numero era", numeroSecreto)
else:
    print("No adivinaste, mi número era", numeroSecreto)
    