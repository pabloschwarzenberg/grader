import random
numero=(random.randint(1, 20))
intentos=0
adivinaste=False
while intentos<5:
  n=int(input('ingrese un numero:'))
  if n==numero:
    intentos=5
    adivinaste=True
    print('Adivinaste, mi número era',numero)
  if numero<n:
    intentos+=1
    print('mi numero es menor')
  if numero>n:
    intentos+=1
    print('mi numero es mayor')
if not adivinaste:
  print('No adivinaste, mi número era',numero)