import random
random_value = random.randrange(1,20)
intentos = 0 
checker = True

while checker:
    guess = int(input('Introduzca su intento: '))
    if guess == random_value:
        print('Adivinaste, mi número era',random_value)
        print('Fin del programa')
        checker = False
    elif guess > random_value:
        print('mi número es menor')
        intentos += 1
        if intentos == 5:
            print('No adivinaste, mi número era',random_value)
            checker = False
    elif guess < random_value:
        print('mi número es mayor')
        intentos += 1
        if intentos == 5:
            print('No adivinaste, mi numero era',random_value)
            checker = False

