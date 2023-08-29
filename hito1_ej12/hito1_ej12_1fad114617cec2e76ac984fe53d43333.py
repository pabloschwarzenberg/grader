import random
numero=random.randint(1,20)
intentos=0
while intentos<5:
    jugador=int(input("ingresa un numero"))
    if jugador>numero:
        print("es menor")
        intentos=intentos+1
    elif jugador<numero:
        print("es mayor")
        intentos=intentos+1
    elif jugador==numero:
        print("Adivinaste, mi numero era"+str(numero))
        intentos=7
if intentos!=7:
    print("No adivinaste, mi numero era "+str(numero))
      