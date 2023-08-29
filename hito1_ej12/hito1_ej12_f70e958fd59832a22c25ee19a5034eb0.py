import random
cont=0
numero_secreto=random.randint(1, 20)
fin=False
while(cont!=5) and(fin!=True):
  n=int(input("¿cual es mi numero secreto?: "))
  if(n==numero_secreto):
    print("Adiviniste, mi numero era ", numero_secreto)
    fin=True
  else:
    if(n<numero_secreto):
      print("Tu numero es menor que el numero secreto")
    if(n>numero_secreto):
      print("Tu numero es mayor al numero secreto")
  cont=cont+1
if(cont==5):
  print("No adivinaste, mi numero era ", numero_secreto)
      