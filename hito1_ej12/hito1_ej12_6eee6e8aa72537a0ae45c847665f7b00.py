#Juego adivina mi número
import random
number_min = 1
number_max = 20
numero_intentos = 0
number = random.randint(number_min,number_max)
print(number)
while numero_intentos < 5:
    guess = int(input('numero: '))
    numero_intentos = numero_intentos +1
    if guess < number:
        print('mi numero es mayor')
    if guess > number:
        print('mi numero es menor')
    if guess == number:
        print('adivinaste mi numero era', number)
    elif numero_intentos > 5:
        break
print('no adivinaste mi numero era', number)      