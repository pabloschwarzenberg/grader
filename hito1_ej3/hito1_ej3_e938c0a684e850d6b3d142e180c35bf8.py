#Aprobación de créditos
pesos=int(input("ingresa tu ingreso en pesos:"))
nacimiento=int(input("ingresa su año de nacimiento:"))
hijos=int(input("ingresa la cantiad de hijos:"))
pertenencia=int(input("ingresa los años de pertenencia al banco:"))
print("C:casado y S:soltero")
estadocivil=input("ingrese su estado civil:")
print("U:urbano y R:rural")
vivienda=input("indique donde vive, campo o ciudad")

if pertenencia>10 and hijos>=2:
  print("APROBADO")

edad=2021-nacimiento

if estadocivil=="C" and hijos>3 and edad>45 or edad<=55:
  print("APROBADO")
elif pesos>2500000 and estadocivil=="S" and vivienda=="U":
  print("APROBADO")
elif pesos>3500000 and pertenencia>5:
  print("APROBADO")
elif vivienda=="R" and estadocivil=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")      