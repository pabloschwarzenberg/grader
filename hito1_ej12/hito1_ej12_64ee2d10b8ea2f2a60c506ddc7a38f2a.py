#Juego adivina mi número
import random
random = random.randint(1,20)
cont= 0
while (cont < 5) :
    cont += 1
    numero = int(input("Porfavor Ingresa tu número :"))
    if numero < random:
        print("mi número es mayor")
    elif numero > random:
        print("mi numero es menor")
    elif numero == random:
         print("Adivinaste, mi número era: {}".format(random))
         break
    elif cont < 5:
         print("No adivinate, mi número era {}".format(random))