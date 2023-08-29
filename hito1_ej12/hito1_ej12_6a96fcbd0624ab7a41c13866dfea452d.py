#Juego adivina mi número
from random import randint
intentos = 5
numero = str(randint(1,20))
while True:
  if intentos < 1:
    print("No adivinaste, mi número era " + numero)
    break
  
  guess = input("Adivina mi número: ")
  if guess == numero:
    print("Adivinaste, mi numero era " + numero)
    break
  
  if int(guess) > int(numero):
    print("mi número es menor")
    intentos -= 1
    continue
    
  if int(guess) < int(numero):
    print("mi número es mayor")
    intentos -= 1
    continue
    
  