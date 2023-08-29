import random
numero_aleatorio=random.randint(1,20)
numero_ingresado=int(input("Ingrese su numero:"))
adivinaste=True
intentos=5
while adivinaste and intentos>=1:
  if numero_ingresado==numero_aleatorio:
    adivinaste=False
    print("Adivinaste, mi número era",numero_aleatorio)
  else:
      if intentos>=1:
       intentos=intentos-1
       adivinaste=True
       numero_ingresado=int(input("Intente otro:"))
if intentos<1:
    print("No adivinaste, mi número era",numero_aleatorio)
   


