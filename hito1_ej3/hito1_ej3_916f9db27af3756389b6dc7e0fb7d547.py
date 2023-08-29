#Aprobación de créditos
sueldo=int(input("ingrese su sueldo: "))
anio=int(input("ingrese su año de nacimiento: "))
hijos=int(input("ingrese cantidad de hijos: "))
banco=int(input("ingrese sus años en el banco: "))
estado=str(input("ingrese su estado civil, S=soltero o C=casado: "))
cc=str(input("ingrese donde se encuentra su vivienda, U=urbano o R=rural: "))
if(banco>10 and hijos>=2):
  print("APROBADO")
if(estado=="C" and hijos>3 and (2020-anio>=45 and 2020-anio<=55)):
  print("APROBADO")
if(sueldo>2500000 and sueldo<3500000 and estado=="S" and cc=="U"):
  print("APROBADO")
if(sueldo>3500000 and banco>5):
  print("APROBADO")
if(cc=="R" and estado=="C" and hijos<2):
  print("APROBADO")      