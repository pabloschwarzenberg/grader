ingresos=int(input("Inserte ingresos del cliente : "))
año=int(input("Ingrese año de nacimiento del cliente : "))
hijos=int(input("Inserte número de hijos del cliente : "))
perte=int(input("Ingrese años de pertenencia al banco : "))
civil=str(input("¿Cliente casado? : "))
camciu=str(input("¿Cliente vive en campo o ciudad? : "))
if perte>=10 and hijos>=2:
    print("APROBADO")
elif civil=="C" and 55>2016-año>45:
    print("APROBADO")
elif ingresos>250000 and civil=="S" and camciu=="U":
    print("APROBADO")
elif ingresos>350000 and perte>5:
    print("APROBADO")
elif (camciu=="R") and (civil=="C") and hijos<2:
    print("APROBADO")
else:
    print("APROBADO")