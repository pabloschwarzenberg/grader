ingreso=int(input("ingresos en pesos:"))
nacimiento=int(input("año de nacimiento:"))
nhijos=int(input("número de hijos:"))
anosenbanco=int(input("años de pertenencia al banco:"))
estado=input("inrese el estado civil (C:casado,S:soltero,):")
vive=input("vive en (R:rural,U:urbano,):")
edad=2020-nacimiento
if anosenbanco>10 and 2<=nhijos:
 print("APROBADO")
elif estado=="C" and 3<nhijos and 45<=edad<=55:
  print("APROBADO")
elif ingreso>3500000 and anosenbanco>5:
   print("APROBADO")
elif vive=="R" and estado=="C" and nhijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")