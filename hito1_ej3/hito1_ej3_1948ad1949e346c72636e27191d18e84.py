#Aprobación de créditos
ingreso=int(input("ingrese su ingreso mensual:"))
ano_nacimiento=int(input("ingrese su año de nacimiento:"))
numero_hijos=int(input("ingrese la cantidad de hijos que tiene:"))
anos_pertenencia=int(input("cuantos años lleva en este banco:"))
estado_civil=str(input("especifique si es soltero o casado:"))
rural_urbano=str(input("especifique si vive en campo o ciudad:"))
edad=2017-ano_nacimiento
if anos_pertenencia>10 and numero_hijos>=2:
  print("APROBADO")
elif estado_civil=="C" and numero_hijos>3 and 45<edad<55:
  print("APROBADO")
elif ingreso>2500000 and estado_civil=="S" and rural_urbano=="U":
  print("APROBADO")
elif ingreso>3500000 and anos_pertenencia>5:
  print("APROBADO")
elif rural_urbano=="R" and estado_civil=="C" and numero_hijos<2:
  print("APROBADO")
else:
  print("REPROBADO")