#Juego adivina mi número
import random

N=random.randint(1,20)
vidas=5
while vidas!=0:
  print(N)
  print("Vidas: ",vidas)
  numero=int(input("Intente adivinar el numero: "))
  if numero == N:
    print("Felicidades a adivinado el numero secreto")
    break
  else:
    vidas=vidas-1
    ("Ese no es el numero")
    if numero<N:
      print("El numero que ingreso es menor al que debe adivinar")
    if numero>N:
      print("El numero que ingreso es mayor al que debe adivinar")
if vidas==0:
  print("Se le acabaron las vidas usted pierde")