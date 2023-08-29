#Juego adivina mi número
import random as rnd
i=0
a=rnd.randrange(20)


for i in range(5):
  i=int(input("Ingrese un numero: "))

  if i<a:
    print("mi número es mayor")
  if i>a:
    print("mi número es menor")
  if i==a:
    break

if i==a:
 print("Adivinaste, mi número era",a)    