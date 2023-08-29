#Aprobación de créditos
print("Bienvenido al sistema de créditos del Banco de Mulchén, por favor ingrese sus datos:")
ingreso = int(input("Ingreso (en pesos y sin puntos):"))
AN = int(input("Año de nacimiento:"))
NH = int(input("Número de hijos:"))
APB = int(input("Años de pertenencia al banco:"))
EC = input("Estado civil (S=Soltero, C=Casado):")
ZV = input("Zona de residencia (U=Urbano, R=Rural):")
if APB>10 and NH>=2:
  print("APROBADO")
if EC=="C" and NH>3 and 1971<=AN and AN<=1961:
  print("APROBADO")
if ingreso>2500000 and EC=="S" and ZV=="U":
  print("APROBADO")
if ingreso>3500000 and APB>5:
  print("APROBADO")
if ZV=="R" and EC=="C" and NH<2:
  print("APROBADO")
else:
  print("REPROBADO")