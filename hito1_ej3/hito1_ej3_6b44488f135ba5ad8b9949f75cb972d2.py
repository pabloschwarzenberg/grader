#Aprobación de créditos
ingreso=int(input("¿Cual es su ingreso?"))
nacimiento=int(input("¿Cual es su año de nacimiento?"))
hijos=int(input("¿Cuantos hijos tiene?"))
pertenencia=int(input("¿Cuantos años lleva perteneciendo al banco?"))
estado=input("¿Cual es su estado civil?")
vivienda=input("¿Vive en campo o ciudad?")

if pertenencia>=10 and hijos >=2:
  print("APROBADO")
if estado=="C" and hijos>=3 and 1962<=nacimiento<=1972:
  print("APROBADO")
if ingreso>=2500000 and estado=="S" and vivienda=="U":
  print("APROBADO")
if ingreso>=3500000 and pertenencia>=5:
  print("APROBADO")
if vivienda=="R" and estado=="C" and hijos<2:
  print("APROBADO")
else:
  print("REPROBADO")