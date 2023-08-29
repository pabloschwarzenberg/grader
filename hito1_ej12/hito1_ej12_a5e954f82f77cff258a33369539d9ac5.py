#Juego adivina mi número
from random import randint
ad=0
i=0
def NumIngresado(numero,rnumero,ad):
  if numero==rnumero:
    ad=1
    return ad
  if numero>rnumero:
    ad=2
    return ad
  if numero<rnumero:
    ad=3
    return ad

rnumero=randint(1,20)
while i<5:
  numero=eval(input('Ingresa el numero: '))
  res=NumIngresado(numero,rnumero,ad)
  if res==2:
    if i==4:
      break
    print('mi número es menor')
  if res==3:
    if i==4:
      break
    print('mi número es mayor')
  if res==1:
    print('Adivinaste, mi número era',rnumero)
    break
  i+=1
if i==4:
  print('No adivinaste, mi número era',rnumero)