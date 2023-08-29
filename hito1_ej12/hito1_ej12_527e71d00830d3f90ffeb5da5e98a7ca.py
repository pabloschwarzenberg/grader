import random
n = random.randint(1,20)
intentos = 0

jugando = True

print("intenta adivinar un numero del 1 al 20")

while jugando:
    intentos += 1
    if intentos <= 5:
        eleccion = int(input("adivina el numero: "))
        if eleccion == n:
            print("Adivinaste, mi número era {}".format(n))
            jugando = False
        elif eleccion > n:
            print("mi número es mayor")
        elif eleccion < n:
            print("mi número es menor")

    else:
      print("No adivinaste, mi número era {}".format(n))
      jugando = False