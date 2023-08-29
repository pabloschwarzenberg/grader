#Juego adivina mi número
import random
numero= random.randint(1,21)
intentos=0
jugando= True

while jugando:
  intentos +=1
  if intentos <=5:
    eleccion=int(input("dime un numero:"))
    if eleccion==numero:
      print("adivinaste mi numero era:",numero)
      jugando= False
    elif eleccion>numero:
      print("mi numero es menor")
    elif eleccion<numero:
      print("mi numero es mayor") 
  else:
    print("no adivinaste, mi numero era:",numero)
    jugando= False