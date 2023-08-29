#Juego adivina mi número
import random
num = random.randrange(1, 21)
intentos = 5
while intentos > 0:
 inte = int(input("ingrese su intento"))
 intentos -= 1
 if num == inte:
  print("Adivinaste, mi número era", num)
 if num > inte:
  print("mi número es menor")
 if num < inte:
  print("mi número es mayor")
if intentos == 0:
 print("No adivinaste, mi número era ", num)
 