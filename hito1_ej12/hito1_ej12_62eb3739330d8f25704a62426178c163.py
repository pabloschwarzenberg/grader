#Juego adivina mi número
import random
ints = 0
v = random.randint(1, 20)
while(ints < 6):
     est = input("Intenta adivinar.")
     est = int(est)  
     ints = ints + 1
     if est < v:
         print('Tu numero es muy bajo.')
     if est > v:
         print('Tu numero es muy alto.')
     if est == v:
          break
if est == v:
    ints = str(ints)
    print("Adivinaste, mi número era ",est)
if est != v:
    print("No adivinaste, mi número era ",v)