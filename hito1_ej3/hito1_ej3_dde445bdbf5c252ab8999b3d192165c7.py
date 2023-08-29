ingreso=int(input("Ingrese sus ingresos en peso $:"))
nacimiento=int(input("Ingrese su año de nacimiento:"))
hijos=int(input("Cantidad de hijos:"))
permanenciaenbanco=int(input("Ingrese sus años de permanencia en el banco:"))
EstadoCivil=input("Estado Civil Casado o Soltero (C/S):")
Livein=input("Vive en Campo (R) o Ciudad (U):")
Edad=2022-nacimiento

if permanenciaenbanco>10 and hijos>=2 or EstadoCivil.upper()=="C" and hijos>3 and Edad>45<55 or ingreso>2500000 and EstadoCivil.upper()=="S" and Livein.upper()=="U" or ingreso>3500000 and permanenciaenbanco>5 or Livein.upper()=="R" and EstadoCivil.upper()=="C" and hijos<2:
  print("APROBADO")
else:
  print("REPROBADO")