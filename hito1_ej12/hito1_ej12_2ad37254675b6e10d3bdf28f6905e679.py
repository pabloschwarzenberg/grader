#mngabler@uc.cl
import random
intentos = 5
numero = random.randint(1, 20)
while intentos > 0:
    x= int(input("a"))
    intentos = intentos - 1
    if x < numero:
      print('muy bajo') 
    if x > numero:
      print('muy alto')
    if x == numero:
         break
if x == numero:
        print('Adivinaste,mi numero era',numero)
if x != numero:
     numero = str(numero)
     print('No adivinaste, mi número era  ',numero)

    