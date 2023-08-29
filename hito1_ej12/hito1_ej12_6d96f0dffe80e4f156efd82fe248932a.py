#Juego adivina mi número
from random import randint

Limite = randint (1, 20)
Oportunidad = 0
Numero = 0 

while Oportunidad <= 5:
      if Oportunidad > 1:
            Numero = int(input("intenta de nuevo: "))
      else:
            Numero = int(input("digita el numero que crees que tengo: "))
      Oportunidad += 1
      if Numero == Limite:
            print("Adivinaste, mi número era", Limite  )
            break
      if  Limite  > Numero:
          print ("Mi número es mayor ")
    
      else:
          print("Mi número es menor ")

      if Oportunidad == 5:
            print("No adivinaste, mi número era", Limite )
            break
    
      else:
          print("Mi número es menor ")

      if Oportunidad == 5:
            print("No adivinaste, mi número era", Limite )
            break   