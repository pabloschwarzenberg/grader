#Aprobación de créditos
Ingreso = int(input("Ingrese su monto en pesos:"))
AN = int(input("Ingrese su año de nacimiento:"))
NH = int(input("Ingrese cantidad de hijos:"))
APB = int(input("Ingrese años de pertenencia al banco]:"))
EC = str(input("Ingrese si es Soltero (S) o casado (C):"))
V = str(input("Ingrese si vive en campo (R) o ciudad (U):"))

ANOACTUAL = 2022
EDAD= ANOACTUAL - AN

if APB > 10 and NH >= 2:
    print("APROBADO")

if str(EC) == "C" and NH > 3 and EDAD > 45 and EDAD < 55:
    print("APROBADO")

if Ingreso > 2500000 and str(EC) == "S" and str(V) == "U":
    print("APROBADO")

if Ingreso > 3500000 and APB > 5:
    print("APROBADO")

if str(V) == "R" and str(EC) == "C" and NH < 2:
    print("APROBADO")

