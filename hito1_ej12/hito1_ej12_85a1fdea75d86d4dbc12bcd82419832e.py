#Juego adivina mi número
import random
guessesTaken = 0
number = random.randint(1,20)

print('Hola, dime un número del 1 al 20. Tienes 5 oportunidades para adivinarlo')
while guessesTaken < 6:
  guess = input ('Cual es tu número?')
  guess = int(guess)
  if guess >= 1 and guess <= 20:
        guessesTaken = guessesTaken + 1
        if guess < number:
            print(str(guessesTaken) +'Muy bajo') 
        if guess > number:
            print(str(guessesTaken) +'Muy alto')
        if guess == number:
            break
  else:
        print('Intenta con otro número')
       
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Excelente !!! Adivinaste mi número era ', number)
   
if guess != number:
    number = str(number)
    print('No adivinaste, mi número era' ,  number)
