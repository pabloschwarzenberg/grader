#Aprobación de créditos
a=int(input("Ingresos en pesos:"))
b=int(input("Año de nacimiento:"))
c=int(input("Numero de hijos:"))
d=int(input("Años de pertenencia al banco:"))
x=input("Estado civil:")
y=input("Sector:")
if d>=10:
    if c>=2:
        print("APROBADO")
    else:
        print("RECHAZADO")
if x=="C":
    if c>=3:
        if 1963<=b<=1973:
            print("APROBADO")
        else:
            print("RECHAZADO")
if a>2500000:
    if x=="S":
        if y=="U":
            print("APROBADO")
        else:
            print("RECHAZADO")
if a>3500000:
    if d>5:
        print("APROBADO")
    else:
        print("RECHAZADO")
if y=="R":
    if x=="C":
        if c<2:
            print("APROBADO")
        else:
            print("RECHAZADO")