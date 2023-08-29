#Aprobación de créditos
ingreso= int(input("Ingrese sus ingresos en peso: "))
nacimiento= int(input("Ingrese su año de nacimiento: "))
hijos= int(input("Ingrese su numero de hijos: "))
años= int(input("Ingrese sus años de pertenencia al banco: "))
estado= input("Ingrese su estado civil S/C soltero o casado: ")
vivienda= input("Ingrese en donde vive U/R urbano o rural: ")
edad= 2021-nacimiento
condicion=0

if años >= 10 and hijos>= 2:
  condicion=1

elif estado=="C" and hijos>3 and edad>=45 and edad<=55:
  condicion=1
elif ingreso>2500000 and estado=="S" and vivienda=="U":
  condicion=1
elif ingreso>3500000 and años>5:
  condicion=1
elif vivienda=="R" and estado=="C" and hijos<2:
  condicion=1

if condicion==1:
  print("APROBADO")
else:
  print("RECHAZADO")      