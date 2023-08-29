#Juego adivina mi número
import random
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
intentos=5
numeroencontrado=False
elnumero=int(random.choice(lista))
while intentos>0 and not numeroencontrado:
  numerojugador=int(input())
  if numerojugador>elnumero:
    print("Tu numero es mayor")
    intentos=intentos - 1
  elif numerojugador<elnumero:
    print("Tu numero es menor")
    intentos=intentos - 1
  else:
    print("Adivinaste, mi numero era:", elnumero)
    numeroencontrado=True
    

