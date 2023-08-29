#Aprobación de créditos
ing=int(input("Ingrese la cantidad de Ingresos: "))
nac=int(input("Ingrese año de nacimiento: "))
hijos=int(input("Ingrese numero de hijos: "))
pert=int(input("Ingrese año de pertenencia al banco: "))
civil=str(input("Ingrese su estado civil: "))
lug=str(input("Ingrese si vive en campo o en ciudad: "))
edad= 2021 - nac

if pert > 10 and hijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
    
if civil == str("C") and hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
else:
    print("RECHAZADO")
    

if ing > 2500000 and civil == str("S") and lug == str("U"):
    print("APROBADO")
else:
    print("RECHAZADO")
    

if ing > 3500000 and pert > 5:
    print("APROBADO")
else:
    print("RECHAZADO")
    

if lug == str("R") and civil == str("C") and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
