from random import*

nro_secreto = randint(1,20)
contador = 0
while contador < 5:
  for contador in range(5):
    num = int(input("ingresa un numero entre 1 y 20 "))
    if num < nro_secreto:
      print("mi numero es mayor")
      contador = contador + 1 
    elif num > nro_secreto:
      print("mi numero es menor")
      contador = contador + 1
    elif num == nro_secreto:
      print("adivinaste mi, numero era ",nro_secreto)
      break
    elif contador == 5:
      print("no adivinaste, mi numero era ",nro_secreto)
      break