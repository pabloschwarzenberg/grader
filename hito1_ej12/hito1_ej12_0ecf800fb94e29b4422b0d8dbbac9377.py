#Juego adivina mi número
from random import randint

Numero_desconocido=randint(1,20)
intento=0
Numero_adivinado=0
while intento<=5:
  if intento>1:
    Numero_adivinado=int(input("intente otra vez: "))
  else:
    Numero_adivinado=int(input("Digita el numero que crees que tengo: "))
  intento+=1
  if Numero_adivinado==Numero_desconocido:
    print("Adivinaste,mi numero era",Numero_desconocido)
    break
  if Numero_desconocido>Numero_adivinado:
    print("Mi numero es mayor")
  else:
    print("Mi numero es menor")
  if intento==5:
    print("No adivinaste,mi numero era",Numero_desconocido)
    break