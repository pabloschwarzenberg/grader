#Juego adivina mi número
import random
a=random.randint(1,20)
n=0
while True:
  x=int(input())
  if(x==a):
    print('Adivinaste, mi numero era' +str(a))
    break
  elif(x<a):
    print('menor')
  elif(x>a):
    print('mayor')
  n=n+1
  if(n==5):
    print('No adivinaste, mi numero era' +str(a))
    break