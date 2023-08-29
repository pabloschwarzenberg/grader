from random import randint

Adivinar = randint (1, 20)

intentos = 0
Adivinado = 0 

while intentos <= 5:
      if intentos > 1:
            Adivinado = int(input("intenta de nuevo: "))
      else:
            Adivinado = int(input("digita el numero que crees que tengo: "))
      intentos += 1
      if Adivinado == Adivinar:
            print("Adivinaste, mi número era", Adivinar )
            break
      if  Adivinar > Adivinado:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if intentos == 5:
            print("No adivinaste, mi número era", Adivinar )
            break      