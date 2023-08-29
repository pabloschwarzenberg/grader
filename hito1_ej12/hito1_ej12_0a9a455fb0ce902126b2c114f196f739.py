
from random import*

oculto = randint(1,20)
oportunidad = 0
num = 0
print(oculto)
while num != oculto and oportunidad < 5:
  print("Oportunidad", oportunidad)
  num = int(input("Ingrese un numero a adivinar entre 1 y 20: "))

  if num > oculto:
    print("Mi numero es menor")
    
  elif num < oculto:
    print("Mi numero es mayor")
    

  oportunidad +=1
if oportunidad >=5:
  print("Has agotado tus oportunidades")
  print("No adivinaste, mi numero es", oculto)
if num == oculto:
  print("Has adivinado!!")