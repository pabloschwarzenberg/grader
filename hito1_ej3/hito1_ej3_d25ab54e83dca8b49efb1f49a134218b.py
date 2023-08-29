a = float(input("ingreso:"))
b = float(input("año de nacimiento:"))
h = float(input("numero de hijos:"))
d = float(input("años de presencia en el banco:"))
e = str(input("estado civil, soltero (S), casado (C):"))
f = str(input("donde vive (U)para ciudad y (R) campo:"))

edad = 2021 - b 

if d>10 and h>=2:
    print("APROBADO")
elif e=="C" and h>3 and 45<=edad>55:
    print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
    print("APROBADO")
elif a>3500000 and d>5:
    print("APROBADO")
elif f=="R" and e=="C" and h<2 :
    print("APROBADO")
else:
    print("RECHAZADO")
