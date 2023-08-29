import random
intentos=0
secreto=random.randint(1,20)
while intentos<5:
  numero=int(input("ingrese un numero"))
  intentos=intentos+1

  if numero<secreto:
    print("tu numero es menor")
  if numero>secreto:
    print("tu numero es mayor")

  if numero==secreto:
    break
if numero==secreto:
  print("Adivinaste, mi número era ",secreto)
else:
  print("No adivinaste, mi número era",secreto)
