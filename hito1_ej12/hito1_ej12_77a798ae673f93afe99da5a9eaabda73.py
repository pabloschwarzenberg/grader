#Juego adivina mi número
nintentos=5
numero=int(input())
for x in range (1,20):
  if 0 < nintentos <= 5:
    if numero<x:
      print("mi numero es menor")
    if numero>x:
      print("mi numero es mayor")
    else:
      print("Adivinaste, mi numero era",x)
      break
    nintentos = nintentos - 1