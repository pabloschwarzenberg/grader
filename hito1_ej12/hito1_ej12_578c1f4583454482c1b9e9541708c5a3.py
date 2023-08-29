#Juego adivina mi número
from random import randint

Numero_Adivinar = randint (1, 20)

intentos = 0
NumeroAdivinado = 0 

while intentos <= 5:
      if intentos > 1:
            NumeroAdivinado = int(input("intenta de nuevo: "))
      else:
            NumeroAdivinado = int(input("digita el numero que crees que tengo: "))
      intentos += 1
      if NumeroAdivinado == Numero_Adivinar:
            print("Adivinaste, mi número era", Numero_Adivinar )
            break
      if  Numero_Adivinar > NumeroAdivinado:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if intentos == 5:
            print("No adivinaste, mi número era", Numero_Adivinar )
            break