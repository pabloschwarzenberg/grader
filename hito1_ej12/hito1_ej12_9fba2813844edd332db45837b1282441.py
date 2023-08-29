#Juego adivina mi número
import random  
 
guessestaken = 0 
 
number = random.randint(1,20)
 
while guessestaken<5:
    guess = int(input("ingresa un numero para comenzar: ")) 
    
    if guess > number:
        print("minúmero  es mayor")
    if guess < number:
        print("mi número es menor")
    if (guess != number) and (guessestaken>5):
        print("No adivinaste, mi número era" + str(number))
    if guess == number: 
        print("Adivinaste, mi número era" + str(number))
        break
    guessestaken = guessestaken + 1 