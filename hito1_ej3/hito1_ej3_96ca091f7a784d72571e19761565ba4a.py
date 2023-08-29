ingreso=int(input("ingresos:"))
nacimiento=int(input("año de nacimiento:"))
hijos=int(input("cantidad de hijos:"))
años=int(input("pertenencia en banco:"))
estado=str(input("estado civil casado:(C), soltero(S)"))
vive=str(input("donde vive urbano(U), rural(R)"))
edad=2020-nacimiento
if años>10 and hijos>1:
  print("APROBADO")
elif estado=="C" and hijos>3 and 55>=edad>=45:
  print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U":
  print("APROBADO")
elif ingreso>3500000 and años>5:
  print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")