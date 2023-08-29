#Aprobación de créditos
ingreso=float(input("Ingrese su dinero:"))
nacimiento=int(input("Ingrese su año de nacimiento:"))
hijos=int(input("Ingrese su numero de hijos:"))
perte=int(input("Ingrese los años de pertenencia een el banco:"))
estado=input("Ingrese su estado civil 'S' para soltero y 'C' para casado:")
vive=input("donde vive? U urbano R rural:")

if perte>10 and hijos>2:
    print("APROBADO")
elif estado=="C" and hijos>3 and nacimiento>1973:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and perte>5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
    print("APROBADO")