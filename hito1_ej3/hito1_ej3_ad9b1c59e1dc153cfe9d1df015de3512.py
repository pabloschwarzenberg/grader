a=int(input("ingreso(en pesos): "))
b=int(input("año de nacimiento: "))
c=int(input("numero de hijos: "))
d=int(input("años de pertenencia al banco: "))
e=str(input("estado civil (S=soltero, C=casado): "))
f=str(input("si vive en campo o ciudad(U=urbano, R=rural): "))
g=2016-b
if d>10 and c>=2:
    print("APROBADO")
elif e==str("C") and c>3 and 45<=g<=55:
    print("APROBADO")
elif a>2500000 and e==str("S") and f==str("U"):
    print("APROBADO")
elif a>3500000 and d<5:
    print("APROBADO")
elif f==str("R") and e==str("C") and c<2:
    print("APROBADO")
else:
    print("RECHAZADO")