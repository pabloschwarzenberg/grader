IG=int(input("ingrese su ingreso en pesos :"))
AÑ=int(input("ingrese edad:"))
NH=int(input("ingrese numero de hijos :"))
APB=int(input("ingrese años de pertenencia al banco :"))
EC=str(input("ingrese estado civil(s=soltero,c=casado) :"))
V=str(input("ingrese Si vive en campo o cuidad ("U": urbano, "R": rural) :"))
EDAD=AÑ-2020

if APB>=10 and NH>=2:
    print("APROBADO")
if EC=="C" and NH>=3 and EDAD>=45 and EDAD<=55:
    print("APROBADO")
if IG>=2500000 and EC=="S" and V=="U":
    print("APROBADO")
if IG>=3500000 and APB>=5:
    print("APROBADO")
if V=="R" and  EC=="C" and NH<=2:
    print("APROBADO")
else:
    print("RECHAZADO")
