#Aprobación de créditos
I=int(input("ingreso(clp):"))
N=int(input("Edad:"))
H=int(input("Hijos:"))
P=int(input("Años en el banco:"))
E=input("Estado civil, S-soltero, C-casado:")
V=input("Urbano(U) o Rural(R):")
if P>=10 and H>=2:
    print("APROBADO")
if E=="C" and H>3 and 55>N>45:
    print("Aprobado")
if I>2500000 and E=="S" and V=="U":
    print("APROBADO")
if I>3500000 and P>5:
    print("APROBADO")
if V=="R" and E=="C" and 2>H:
    print("APROBADO")
else:("REPROBADO")  