#Juego adivina mi número
import random
numero = random.randint(1,20)
intentos = 5
print(numero)
validar = False

while validar == False:
  num_User = int(input("Indique un número:"))
  if num_User < numero:
    print("Mi número es mayor")
    intentos -= 1
  elif num_User > numero:
    print("Mi número es menor")
    intentos -= 1
  else:
    print("Adivinaste, mi número era {}".format(numero))
    validar = True
  if intentos == 0:
    print("No adivinaste, mi número era {}".format(numero))
    validar = True