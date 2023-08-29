import random
intentos = 0
minimo = 1
maximo = 20
numero_random = random.randint(1,20)
print("Bienvenido al juego Adivina mi número, como lo dice\nel nombre tienes que divinar el numero en que que estoy pensando ")
print("\nEl numero estara entre el 1 y el 20, ¡A JUGAR!")
while intentos < 5:
    print("Ingresa el numero que crees que pienso")
    numero = input()
    numero = int(numero)

    intentos = intentos + 1
    if numero == numero_random:
        print("Adivinaste, mi número era", numero_random)
        break
    elif numero != numero_random:
            if numero < numero_random:
                print("mi número es mayor")
            else:
                if numero > numero_random:
                    print("mi número es menor")

else:
    print("No adivinaste, mi número era", numero_random)