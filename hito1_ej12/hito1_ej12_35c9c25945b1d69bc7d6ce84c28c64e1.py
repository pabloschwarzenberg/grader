#Juego adivina mi número
from random import randint

Nincognito = randint(1, 20)

intentos = 0
Ncorrecto = 0 

while 5 >= intentos:
      if intentos > 1:
            Ncorrecto = int(input("intentar otra vez= "))
      else:
            Ncorrecto = int(input("Ingresa el numero que tienes en mente= "))
      intentos += 1
      if Ncorrecto == Nincognito:
            print("Adivinaste, mi numero era", Nincognito )
            break
      if  Ncorrecto < Nincognito:
          print ("Mi numero es mayor")
    
      else:
            print("Mi numero es menor")

      if intentos == 5:
            print("No adivinaste, mi número era", Nincognito)
            break
      