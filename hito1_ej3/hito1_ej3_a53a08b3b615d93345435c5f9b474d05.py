#Aprobación de créditos
ingreso = int (input("ingrese su ingreso en pesos: "))
ano_nacimiento = int (input("ingrese año de nacimiento: "))
cant_hijos = int (input("ingrese cuantos hijos tiene: "))
anos_pertenencia = int (input("ingrese los años de pertenencia: "))
estado_civil = input("ingrese su estado civil, S=soltero y C=casado:  ")
lugar_residencia = input("ingrese si vive en campo o ciudad (R=rural y U=urbano): ")

aprobado = False

if anos_pertenencia>10 and cant_hijos>=2:
  aprobado=True
elif estado_civil=="C" and cant_hijos>3 and 45<=(2023-ano_nacimiento)<=55:
  aprobado=True
elif ingreso > 2500000 and estado_civil=="S" and lugar_residencia=="U":
  aprobado=True
elif ingreso>3500000 and anos_pertencia>5:
  aprobado=True
elif lugar_residencia=="R" and estado_civil=="C" and cant_hijos<2:
  aprobado=True

if aprobado:
   print("APROBADO")
else:
   print("RECHAZADO")