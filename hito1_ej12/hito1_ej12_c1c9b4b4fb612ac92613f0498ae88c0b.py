import random
print ('Bienvenido')
n=random.randrange(1,20)
ni=0
x=int(input('ingrese un numero entero entre 1 y 20:'))
while ni<5:
  if x<n:
    print('el numero ingresado es menor')
  elif x>n:
    print('el numero ingresado es mayor')
  elif x==n:
    print('felicidades adivinaste, mi nuero era:',n)
    break
  ni+=1
if ni==5:
  print('no adivinaste, mi nuero era',n)