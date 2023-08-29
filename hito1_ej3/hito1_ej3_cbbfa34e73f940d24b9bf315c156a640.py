#Aprobación de créditos
ingreso=int(input("Ingreso: "))
año=int(input("Año de nacimiento: "))
hijos=int(input("Numero de hijos "))
apb=int(input("Años de pertenencia al banco: "))
estado=str(input("estado civil: "))
c2=str(input("¿Vive en el campo o en la ciudad? "))
años = 2023-año
if apb>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 45<años<55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and c2=="U":
    print("APROBADO")
elif ingreso>3500000 and apb>5:
    print("APROBADO")
elif c2=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")