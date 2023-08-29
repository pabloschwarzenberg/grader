#Juego adivina mi número
from random import randint

x = randint (1, 20)
i = 0
y = 0 
while i <= 5:
      if i > 1:
            y = int(input("prueba con otro numero: "))
      else:
            y = int(input("adivina el numero: "))
      i += 1
      if y == x:
            print("Adivinaste, mi número era", x )
            break
      if  x > y:
          print ("Mi número es mayor ")
      else:
            print("Mi número es menor ")
      if i == 5:
            print("No adivinaste, mi número era", x )
            break
