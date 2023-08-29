#Juego adivina mi número
from random import randint

NumeroParaAdivinar = randint (1, 20)

intentos = 0
NumeroAdivinado = 0 

while intentos <= 5:
      if intentos > 1:
            NumeroAdivinado = int(input("intenta de nuevo: "))
      else:
            NumeroAdivinado = int(input("digita el numero que crees que tengo: "))
      intentos += 1
      if NumeroAdivinado == NumeroParaAdivinar:
            print("Adivinaste, mi número era", NumeroParaAdivinar )
            break
      if  NumeroParaAdivinar > NumeroAdivinado:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if intentos == 5:
            print("No adivinaste, mi número era", NumeroParaAdivinar )
            break   