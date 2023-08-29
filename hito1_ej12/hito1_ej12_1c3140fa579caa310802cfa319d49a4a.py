#Juego adivina mi número

from random import*
x=[]

y=randint(1,20)
x.append(y)

print('Solo tienes 5 intentos para adivinar mi numero (entre 1 y 20).','\n')

for i in range(5):
  num=int(input('Adivina mi numero:'))

  if num>x[0]:
    print('Mi numero es menor')

  elif num<x[0]:
    print('Mi numero es mayor')

  elif num==x[0]:
    print('Adivinaste, mi numero era:',x[0])
    break

else:
  print('No adivinaste, mi numero era:',x[0])