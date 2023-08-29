IP=-1
while (IP<0):
  IP=int(input("ingrese su ingreso mensual (en pesos) "))
adn=0
while (adn<=2002 and adn>=1922):
  año=int(input("Por favor, ingrese su fecha de nacimiento "))
NH=-1
while (NH<=0):
  NH=int(input("¿cuantos hijos tiene? "))
apb=-1
while (apb<=0):
  apb=int(input("¿cuantos años lleva perteneciendo al banco "))
EC=-1
while (EC<0):
  EC=input("¿cual es su estado civil? (responder con S para soltero y C para casado) ")
CC=-1
while (CC<0):
  CC=input("en donde se ubica su residencia, ¿en campo o ciudad? (responda con U para urbano y R para rural")
  if (apb > 10 and NH >=2):
      print("APROBADO")
  elif (EC == "C" and "NH" > 3 and año<55 and año > 45):
      print("APROBADO")
  elif (IP > 2500000 and EC == "C" and CC == "U"):
      print("APROBADO")
  elif (IP > 3500000 and apb > 5):
    print("APROBADO")
  elif (CC == "R" and EC == "C" and NH < 2):
    print("APROBADO")
  else:
    print("RECHAZADO")