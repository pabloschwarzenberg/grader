import random

a = random.randint(1, 20)

print(
    "El juego comienza cuando eligo un número al azar entre el 1 y el 20. Tu debes tratar de adiniar para ganar. Tienes 5 oportunidades")
print("Buena suerte.")

turno = 5

while turno != 6:
    turno -= 1
    intentos = int(input("Ingrese número:"))
    if intentos == a:
        print("Adivinaste, mi número era", a)
        turno += 1
        break
    elif intentos < a:
        print("El número elegido es muy pequeño")
    elif intentos > a:
        print("El número elegido es muy grande")

if turno == 0:
    print("No adivinaste, mi número era", a)
      