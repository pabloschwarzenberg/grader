#Juego adivina mi número
from random import randint
NumeroSecreto = randint (1, 20)
intentos = 0
NumeroAdivinado = 0 

while intentos <= 5:
      if intentos > 1:
            NumeroAdivinado = int(input("intenta de nuevo: "))
      else:
            NumeroAdivinado = int(input("digita el numero que crees que tengo: "))
      intentos += 1
      if NumeroAdivinado == NumeroSecreto:
            print("Adivinaste, mi número era", NumeroSecreto)
            break
      if  NumeroSecreto > NumeroAdivinado:
          print ("Mi número es mayor ")   
      else:
            print("Mi número es menor ")
      if intentos == 5:
            print("No adivinaste, mi número era", NumeroSecreto)
            break