#Juego adivina mi número
import random
contador = 1
while contador >= 1:
      contador = contador + 1
      n = random.randint(1, 20)
      attemp = int(input("Ingrese un numero : "))
      if attemp > n :
         print("mi número es menor")

      if attemp < n :
         print("mi número es mayor")

      if attemp  == n :
        print("Adivinaste, mi número era", n)

        break
      if contador == 6 :
        print("No adivinaste, mi número era", n)
        break      