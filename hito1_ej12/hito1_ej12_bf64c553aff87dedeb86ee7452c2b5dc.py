#Juego adivina mi número
      import random

juego=0
minnum=1
maxnum=20

numero=random.randint(minnum,maxnum)

print("Piensa en un numero entre", str(minnum)+ "y"  +str(maxnum))
while juego < 5:
  print("adivina:")
  adivina=int(input())
  
  juego=juego+1

  if adivina<numero:
    print("mi numero es mayor")
  if adivina>numero:
    print(" mi numero es menor")
  if adivina==numero:
    break

if adivina==numero:
  print("adivinaste,mi numero era:", adivina)
if adivina != numero:
  print("no adivinaste,mi numero era,numero")
  