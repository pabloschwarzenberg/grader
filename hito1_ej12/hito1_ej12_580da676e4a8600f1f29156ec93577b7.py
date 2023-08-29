#Juego adivina mi número
import random

intentos = 0
numeroMin = 1
numeroMax = 20

num = random.randint(numeroMin, numeroMax)
while intentos < 5:
      print("Intenta adivinar: ")
      adivinar = input()
      adivinar = int(adivinar)
      
      intentos = intentos + 1
      
      if adivinar < num:
          print("mi número es mayor")
      if adivinar > num:
          print("mi número es menor")
      if adivinar == num:
          break
if adivinar == num:
    num = str(num)
    print("Adivinaste, mi número era" + num)
if adivinar != num:
    num = str(num)
    print("No adivinaste, mi número era" + num)
