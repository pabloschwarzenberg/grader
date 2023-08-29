#Aprobación de créditos
D=float(input("Ingreso en pesos:"))
N=int(input("Año de nacimiento:"))
H=int(input("n° de hijos:"))
B=int(input("años de pertenencia al banco:"))
E=str(input("estado civil (S o C):"))
V=str(input("donde vive (U o R):"))
if B>10 and H>=2:
    print("APROBADO")
if E=="C" and H>3 and (2018-N)<=55 and (2018-N)>=45:
    print("APROBADO")
if D>2500000 and E=="S" and V=="U":
    print("APROBADO")
if D>3500000 and B>5:
    print("APROBADO")
if V=="R" and E=="C" and H<2:
    print("APROBADO")

else:
    print("RECHAZADO")      