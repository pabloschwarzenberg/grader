#Aprobación de créditos
Ingreso=int(input("Ingresos: "))
AN=int(input("Año de nacimiento: "))
Edad=(2018-AN)
Hijos=int(input("Número de hijos: "))
AP=int(input("Años de pertenencia al banco: "))
EC=input("Estado civil (S o C): ")
V=input("Vivienda (R o U): ")
if AP>10 and Hijos>=2:
  print("APROBADO")
elif EC=="C" and Hijos>3 and 45<Edad<55:
  print("APROBADO")
elif Ingreso>2500000 and EC=="S" and V=="U":
  print("APROBADO")
elif V=="R" and EC=="C" and Hijos<2:
  print("APROBADO")
elif Ingreso>3500000 and AP>5:
  print("APROBADO")