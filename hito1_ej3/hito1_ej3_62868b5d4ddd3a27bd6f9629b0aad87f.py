#Aprobación de créditos
i=int(input("ingresos:"))
a=int(input("año de nacimiento:"))
h=int(input("numero de hijos:"))
p=int(input("años de pertenencia al banco:"))
e=(input("estado civil:"))
v=input("residencia:")
S="soltero"
C="casado"
U="urbano"
R="rural"

años=2016-a
if p==10 and h>=2:
    print("APROBADO")
if e==C and h>3 and 45<=años<=55:
    print("APROBADO")
if i<2500000 and e==S and v==U:
    print("APROBADO")
if i<3500000 and p>5:
    print("APROBADO")
if v==R and e==C and h<2:
    print("APROBADO")
else:
    print("RECHAZADO")
    
      