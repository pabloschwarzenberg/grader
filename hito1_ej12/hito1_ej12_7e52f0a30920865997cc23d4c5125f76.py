#Juego adivina mi número
from random import randint

NroParaAdivinar = randint (1, 20)

intentos = 0
NroAdivinado = 0 

while intentos <= 5:
      if intentos > 1:
            NroAdivinado = int(input("intenta de nuevamente: "))
      else:
            NroAdivinado = int(input("Escribe el numero que crees que tengo: "))
      intentos += 1
      if NroAdivinado == NroParaAdivinar:
            print("Acertaste, mi número era", NroParaAdivinar )
            break
      if  NroParaAdivinar > NroAdivinado:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if intentos == 5:
            print("No acertaste, mi número era", NroParaAdivinar )
            break