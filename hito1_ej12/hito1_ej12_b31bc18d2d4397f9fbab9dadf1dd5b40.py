import random

randomNumber = 12
intentos = 0
while (intentos <= 5):
    number = input("")
    number = int(number)
    if number == randomNumber:
        print('Adivinaste, mi número era ' + str(randomNumber))
        intentos = 7
    else:
        if number > randomNumber:
            print('mi número es mayor')
            intentos += 1
        if number < randomNumber:
            print('mi número es menor')
            intentos +=1
if intentos == 6:
    print('No adivinaste, mi número era' + str(randomNumber))