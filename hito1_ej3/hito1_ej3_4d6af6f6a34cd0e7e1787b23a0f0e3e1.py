I=int(input("Ingreso (en pesos):"))
A=int(input("Año de nacimiento:"))
H=int(input("Número de hijos:"))
P=int(input("Años de pertenencia al banco:"))
E=str(input("Estado civil soltero(S) o casado(C):"))
Casa=str(input("Si vive en campo(R) o ciudad(U):"))
Edad=2016-A

if P>10 and H>=2:
   print("APROBADO")
if E=="C" and H>3 and 45<Edad<55:
   print("APROBADO")
if I>2500000 and E=="S" and Casa=="U":
   print("APROBADO")
if I>3500000 and P>5:
   print("APROBADO")
if Casa=="R" and E=="C" and H<2:
   print("APROBADO") 
if Casa=="R" and E=="C" and H<2:
   print("APROBADO")
