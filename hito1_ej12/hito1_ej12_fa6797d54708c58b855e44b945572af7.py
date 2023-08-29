#Juego adivina mi número
 from random import randint

NumeroporAdivinar = randint (1, 20)

intentos = 0
Numeroadivinado = 0 

while intentos <= 5:
      if intentos > 1:
            Numeroadivinado = int(input("intenta de nuevo: "))
      else:
            Numeroadivinado = int(input("digita el numero que crees que tengo: "))
      intentos += 1
      if Numeroadivinado == NumeroporAdivinar:
            print("Adivinaste, mi número era", NumeroporAdivinar )
            break
      if  NumeroporAdivinar > Numeroadivinado:
          print ("Mi número es mayor ")
    
      else:
            print("Mi número es menor ")

      if intentos == 5:
            print("No adivinaste, mi número era", NumeroporAdivinar )
            break     