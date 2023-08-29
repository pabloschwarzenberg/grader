#Juego adivina mi número
from random import randint
num = randint(0,20)
numjur = 0
i = 0
while i < 5 and (numjur != num):
  numjur = int(input("Ingrese su numero: "))
  i = i+1
  if num > numjur:
      print("mi número es mayor")
  if num < numjur:
      print("mi número es menor")
  if numjur == num:
    print("Adivinaste, mi número era", num)


if numjur != num:
  print("No adivinaste, mi número era", num)   