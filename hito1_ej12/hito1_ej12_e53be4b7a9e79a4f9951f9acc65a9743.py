#Juego adivina mi número
import random
num_random = random.randrange(1,21)
intentos = 0
while intentos < 5:
    numero = int(input('Ingresa el numero: '))
    if numero > num_random:
        print("mi número es menor")
        intentos+=1
    if numero < num_random:
        print("mi número es mayor")
        intentos+=1
    if numero == num_random:
        print("Adivinaste, mi número era", num_random)
        intentos+=5
    if numero != num_random and intentos == 5:
        print("Perdiste, mi número era", num_random)        