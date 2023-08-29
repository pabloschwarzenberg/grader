#Aprobación de créditos
Ingreso=int(input("Ingrese cuanto es su sueldo"))
Ano_nacimiento=int(input("Ingrese año de nacimiento "))
Numero_hijos=int(input("Ingrese cuantos hijos tiene "))
Anos_pertenencia=int(input("Ingrese la cantidad de años que pertenece al banco "))
Estado_civil=input("Ingrese ´C´ si es Casado y ´S´ si es soltero ")
Vive=input("Ingrese ´U´ si vive en área urbana y ´R´ si es en zona Rural")
Edad=2018-Ano_nacimiento

if Anos_pertenencia>10 and Numero_hijos>1:
      print("APROBADO")
if Estado_civil=="C" and Numero_hijos>2 and Edad>45 and Edad<56:
      print("APROBADO")
if Ingreso>2500000 and Estado_civil=="S" and Vive=="U":
      print("APROBADO")
if Ingreso>3500000 and Anos_pertenencia>5:
      print("APROBADO")
if Vive=="R" and Estado_civil=="C" and Numero_hijos<2 and Numero_hijos>-1:
      print("APROBADO")
else:
      print("REPROBADO")

"""
Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
"""