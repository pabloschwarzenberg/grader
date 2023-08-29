#Juego adivina mi número
import random
nro=random.randint(1,20)
adivino=False
for i in range(5):
  adiv=int(input())
  if(adiv==nro):
    print("Adivinaste, mi numero era",nro)
    adivino=True
    break
  elif(adiv<nro):
    print('menor')
  else:
    print('mayor')
if(not adivino):
  print('No adivinaste, mi numero era',nro)