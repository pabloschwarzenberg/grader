#Aprobación de créditos
P = int(input("Ingrese sus ingresos en pesos:"))
A = int(input("Ingrese su año de nacimiento:"))
N = int(input("Ingrese el numero de hijos:"))
AB = float(input("Ingrese años de pertenencia al banco:"))
E = (input("Ingrese su Estado Civil:"))
V = (input("Ingrese si vive en campo o ciudad:"))

if AB > 10 and N >= 2:
    print("APROBADO")
if N > 3 and E == "C" and A <= 1966 or A >= 1976:
    print("APROBADO")
if P > 2500000 and E == "S" and V == "U":
    print("APROBADO")
if P > 3500000 and AB > 5:
    print("APROBADO")
if V == "R" and E == "C" and N < 2:
    print("APROBADO")