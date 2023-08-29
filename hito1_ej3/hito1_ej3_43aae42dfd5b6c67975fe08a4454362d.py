#Aprobación de créditos
Ingreso=int(input())
Nacimiento=int(input())
Hijos=int(input())
Pertenencia=int(input())
Estado=str(input())
C=str
S=str
Lugar=str(input())
R=str
U=str
if Pertenencia>10 and Hijos>=2:
  print("APROBADO")
elif Estado=="C" and Hijos>3 and 1963<Nacimiento<1973:
  print("APROBADO")
elif 2500000<Ingreso and Estado=="S" and Lugar=="U":
  print("APROBADO")
elif 3500000<Ingreso and Pertenencia>5:
  print("APROBADO")
elif Lugar=="R" and Estado=="C" and Hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")