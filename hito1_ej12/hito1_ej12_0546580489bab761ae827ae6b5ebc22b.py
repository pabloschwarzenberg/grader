#Juego adivina mi número
import random as rand

rand_num = rand.randint(1, 21)
num_ingresado = 0
intentos = 5
print(rand_num)
while num_ingresado != rand_num:
    print("intentos restantes:", intentos)
    num_ingresado = int(input("Adivina mi numero: "))
    intentos -= 1
    if intentos == 0:
        break

if num_ingresado == rand_num:
    print("Adivinaste, mi número era {0}".format(rand_num))
else:
    print("No adivinaste, mi número era {0}".format(rand_num))
