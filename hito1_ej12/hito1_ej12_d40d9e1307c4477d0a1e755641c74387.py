#Juego adivina mi número
from random import randint

NumeroaAdivinar = randint (1, 20)

intentos = 0
ElNumeroAdivinado = 0 

while intentos <= 5:
      if intentos > 1:
            ElNumeroAdivinado = int(input("vuelve a intentarlo: "))
      else:
            NumeroAdivinado = int(input("escribe el numero que podria tener: "))
      intentos += 1
      if ElNumeroAdivinado == NumeroaAdivinar:
            print("Adivinaste, mi número era", NumeroaAdivinar )
            break
      if  NumeroaAdivinar > ElNumeroAdivinado:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if intentos == 5:
            print("No adivinaste, mi número era", NumeroaAdivinar )
            break     