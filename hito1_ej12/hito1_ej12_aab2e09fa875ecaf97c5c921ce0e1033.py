#Juego adivina mi número
from random import randint

NumParaAdivinar = randint (1, 20)

intentos = 0
NumAdivinado = 0 

while intentos <= 5:
      if intentos > 1:
            NumAdivinado = int(input("Intenta otra vez: "))
      else:
            NumAdivinado = int(input("¿Que número crees que tengo?: "))
      intentos += 1
      if NumAdivinado == NumParaAdivinar:
            print("Adivinaste, mi número era", NumParaAdivinar )
            break
      if  NumParaAdivinar > NumAdivinado:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if intentos == 5:
            print("No adivinaste, mi número era", NumParaAdivinar )
            break