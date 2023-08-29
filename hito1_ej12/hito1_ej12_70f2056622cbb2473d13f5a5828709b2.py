#Juego adivina mi número
import random 
intento = 0
numero_aleatorio = random.randint(1, 20)
r = True
print("Vamos a jugar adivina el numero, yo pienso un numero y tu tienes que adivinarlo")
guess = int(input("En que numero estoy pensando?: "))
while True:
    intento = intento + 1
    if intento == 6:
        print("¡Noo! ¡Te equivocaste!, el numero era: ", numero_aleatorio)
        break
    elif guess == numero_aleatorio:
        print("¡Bien hecho!, adivinaste, mi numero era ", numero_aleatorio)
        break
    elif guess != numero_aleatorio:
        pista = guess - numero_aleatorio
        if pista < 0:
            print("Frio, mi numero es mayor que ", guess)
        if pista > 0:
            print("Tibio, mi numero es menor que eso ", guess)
         