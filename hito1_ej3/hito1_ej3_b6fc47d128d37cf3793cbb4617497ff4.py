a=int(input("Ingresos:"))
b=int(input("Año de nacimiento:"))
c=int(input("Numero de hijos:"))
d=int(input("Años de pertenencia al banco:"))
e=str(input("Estado civil:"))
f=str(input("Vive en:"))
if d>10 and c>=2:
    print("APROBADO")
elif e=="C" and b>=1961 and b<=1971:
    print("APROBADO")
elif a>=2500000 and e=="S" and f=="U":
    print("APROBADO")
elif a>=3500000 and d>5:
    print("APROBADO")
elif f=="R" and e=="C" and c<2:
    print("APROBADO")
else:
    print("RECHAZADO")      