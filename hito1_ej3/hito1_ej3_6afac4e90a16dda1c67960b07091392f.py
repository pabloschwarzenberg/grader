ingreso= eval(input("Ingrese su dinero $"))
año_nac= eval(input("Año de nacimiento:"))
año= 2020-año_nac
hijos= eval(input("Ingrese Numero de hijos:"))
pertenecia_banco= eval(input("Ingrese años de pertenecia al banco:"))
print("Escoja una opcion\nS.Soltero\nC.Casado")
Estado_civil=input("Ingresa una opcion:")
print("Escoja una opcion\nU.Urbano\nR.Rural")
lugar=input("Ingresa una opcion:")
if pertenecia_banco>10 and hijos>=2:
  print("Aprobado")
elif Estado_civil== "C" and hijos>3 and año>=45 and año<55:
  print("Aprobado")
elif ingreso>2500000 and Estado_civil=="S" and lugar=="C":
  print("Aprobado")
elif ingreso>3500000 and pertenecia_banco> 5:
  print("Aprobado")
elif lugar== "R" and Estado_civil=="C" and hijos<2:
  print("Aprobado")
else:
  print("Rechazado")