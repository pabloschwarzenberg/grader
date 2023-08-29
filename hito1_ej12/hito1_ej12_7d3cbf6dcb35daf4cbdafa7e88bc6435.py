#Juego adivina mi número
i=0
import random
num = random.randint(1,20)

while (i<=4):
  numj= int(input('Inserte un número entre el 1 y el 20: '))

  if numj < num:
    print('El numero ingresado es menor que el número secreto')
    i = i+1

  elif numj > num:
    print('El numero ingresado es mayor que el número secreto')
    i = i+1

  elif numj == num:
      print('Adivinaste, mi número era',num)

if i==5:
    print('No adivinaste, mi número era ',num)