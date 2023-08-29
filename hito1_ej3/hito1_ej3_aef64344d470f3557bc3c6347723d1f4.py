#Aprobación de créditos
I=int(input("Ingrese el Ingreso:"))
A=int(input("Ingrese el año de nacimiento:"))
N=int(input("Ingrese el numero de hijos:"))
AP=int(input("Ingrese el o los años de pertenencia al banco:"))
EC=input("Ingrese el estado civil:")
V=input("Ingrese si vive en campo o ciudad:")

if AP>10 and N>=2:
  print("APROBADO")
elif EC=="C" and N>3 and 45<(2016-A)<55:
  print("APROBADO")
elif I>2500000 and EC=="S" and V=="U":
  print("APROBADO")
elif I>3500000 and AP>5:
  print("APROBADO")
elif V=="R" and EC=="C" and N<2:
  print("APROBADO")
else:
  print("RECHAZADO")