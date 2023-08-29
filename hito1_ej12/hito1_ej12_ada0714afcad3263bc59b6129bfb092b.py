#Juego adivina mi número
from random import*
NUM = randint(1, 20) 
j = 0 
while j <= 5: 
  inten = int(input("Ingresa un numero aleatorio:"))
  if inten > NUM:
    print("El numero secreto es menor:") 
    j = j + 1
  elif  inten < NUM: 
    print("El numero secreto es mayor:")
    j = j + 1
  if inten == NUM: 
    print("Adivinaste correctamente mi numero, era:", NUM)
    break 
  if j == 5: 
    print("No adivinaste correctamente mi numero, era:", NUM)
    break      