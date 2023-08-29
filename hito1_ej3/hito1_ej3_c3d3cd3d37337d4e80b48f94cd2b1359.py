#Aprobación de créditos
Ingreso = int(input("Ingrese su ingreso en pesos "))
Nacimiento = int(input("Ingrese su año de nacimiento "))
Edad = 2021 - Nacimiento
Hijos = int(input("Ingrese la cuantos hijos tiene "))
Asociado = int(input("Ingrese cuantos años ha permacido en este banco "))
Estadocivil = input("Soltero o Casado S/C ")
while(Estadocivil != "S" and Estadocivil != "C" ):
 Estadocivil= input("opciones A,B")
if Estadocivil == "S":
  print("ES S")
elif Estadocivil == "C":
  print("ES C")
Vivencia = input("Urbano o Rural U/R ")
while(Vivencia != "U" and Vivencia != "R" ):
  opcion = input("opciones A,B")
if Vivencia == "U":
  print("ES U")
elif Vivencia == "R":
  print("ES R")
if Asociado > 10:
 if Hijos >= 2:
   print("APROBADO")
 else:
   print("RECHAZADO")
if Estadocivil=="C":
  if Hijos>3:
    if Edad>= 45 and Edad<=55:
      print("APROBADO")
  else:
   print("RECHAZADO")
if Ingreso > 2500000:
  if Estadocivil=="S":
   if Vivencia == "U":
    print("APROBADO")
  else:
    print("RECHAZADO")
if Ingreso>3500000 and Asociado>5:
  print("APROBADO")
else:
  print("RECHAZADO")
if Vivencia== "R" and Estadocivil== "C" and Hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")