#Aprobación de créditos
Ingreso=int(input("Ingreso:"))
Año=int(input("Año de nacimiento:"))
N=int(input("Número de hijos:"))
A=int(input("Años de banco:"))
E=str(input("Estado civil(C=casado o S=soltero):"))
L=str(input("Si vive en campo o ciudad(U=urbano o R=rural):"))

if A>10 and N>=2:
    print("APROBADO")
elif E=="C" and N>3 and 2017-Año>=45 and 2017-Año<=55:
    print("APROBADO")
elif Ingreso>2500000 and E=="S" and L=="U":
    print("APROBADO")
elif Ingreso>3500000 and A>5:
    print("APROBADO")
elif L=="R" and E=="C" and N<2:
    print("APROBADO")
else:
    print("DESAPROBADO")