import random
n=random.randint(1, 20)
t=0
while t<5:
    j=int(input('Ingrese el numero'))
    if j<n:
        print('mi número es mayor')
    if j>n:
        print('mi número es menor')
    if j==n:
        print('Adivinaste, mi número era ',n)
        break
    t += 1
    if t==5:
        print('No adivinaste, mi número era ',n)
      