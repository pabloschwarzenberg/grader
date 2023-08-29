#Juego adivina mi número
from random import randint

numaleatorio = randint(1,20)
intentos = 5

while True:
  numentrada = int(input("Intenta adivinar mi numero: "))
  if (numaleatorio == numentrada):
    print("Adivinaste,mi numero era: " , numaleatorio)
    break
  
  if (intentos == 0):
    print("No adivinaste,mi numero era: " , numaleatorio)
    break
    
  elif (numaleatorio != numentrada):
    if (numaleatorio > numentrada):
      print("Mi numero es mayor")
    elif (numaleatorio < numentrada):
      print("Mi numero es menor")
  intentos -= 1    