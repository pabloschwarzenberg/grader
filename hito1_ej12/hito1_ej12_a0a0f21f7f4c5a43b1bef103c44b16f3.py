import random
numero_secreto = random.randint(1,20)
ganar = False
for i in range(1,6):
    numero_ingresado = int(input("ingrese numero entre 1 y 5: "))
    if numero_secreto == numero_ingresado:
        ganar = True
        break
if ganar:
    print("Adivinaste,mi numero era ",numero_secreto)
else:
    print("No adivinaste, mi numero era ", numero_secreto)