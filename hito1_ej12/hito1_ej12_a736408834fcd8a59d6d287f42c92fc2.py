from os import system
import random
system ("cls")
intento = 0
numero_aleatorio = random.randint(1, 20)
r = True
print("Vamos a jugar a adivinar el numero, yo pienso un numero y tu lo tienes que adivinar en un maximo ded 5 intentos, a jugar!!")
while True:
    intento = intento + 1
    if intento == 6:
        print("No adivinaste, mi numero era ",numero_aleatorio)
        break
    guess= int(input("En que numero estoy pensando?: "))
    if guess == numero_aleatorio:
        print("Adivinaste, mi número era ",numero_aleatorio)
        break
    if guess != numero_aleatorio:
        pista = guess - numero_aleatorio
        if pista < 0:
            print("mi numero es mayor que ", guess)
        if pista > 0:
            print("mi numero es menor que ",guess)