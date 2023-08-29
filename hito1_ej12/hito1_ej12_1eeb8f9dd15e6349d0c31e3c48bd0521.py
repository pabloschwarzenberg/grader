#Juego adivina mi número
from random import randint

NumAdivinar = randint (1, 20)

intentos = 0
NumAdivinado = 0 

while intentos <= 5:
      if intentos > 1:
            NumAdivinado = int(input("intenta de nuevo: "))
      else:
            NumAdivinado = int(input("digita el número que crees que tengo: "))
      intentos += 1
      if NumAdivinado == NumAdivinar:
            print("Adivinaste, mi número era", NumAdivinar )
            break
      if  NumAdivinar > NumAdivinado:
          print ("Mi número es mayor ")
      else:
            print("Mi número es menor ")
      if intentos == 5:
            print("No adivinaste, mi número era", NumAdivinar )
            break
