#Aprobación de créditos
ingreso=int(input("Ingrese sus ingresos: "))
año=int(input("Año de nacimiento: "))
hijos=int(input("Numero de hijos: "))
antbanc=int(input("Años de antiguedad al banco: "))
estado=input("Estado civil(S:soltero, C:casado): ").upper()
casa=input("Si vive en campo o ciudad(U:urbano, R:rural): ").upper()
nacimiento=2022-año
if antbanc>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and nacimiento>45 and nacimiento<55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and casa=="U":
    print("APROBADO")
elif ingreso>3500000 and antbanc>5:
    print("APROBADO")
elif casa=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")