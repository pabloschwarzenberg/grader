#Aprobación de créditos
ingreso = int(input("Ingrese sus ingresos: "))
añoN = int(input("Ingrese su año de nacimiento: "))
nH = int(input("Ingrese su número de hijos: "))
aP = int(input("Ingrese sus años de pertenencia al banco: "))
eC = str(input("Ingrese su estado civil ('S' si es soltero o'C' si es casado): "))
uR = str(input("Ingrese donde vive ('U' si es urbano o'R' si es rural): "))
edad = (2020-añoN)

if (aP > 10) and (nH >= 2):
    print("APROBADO")

elif (eC == "C") and (nH > 3) and (45<=edad<=55):
    print("APROBADO")

elif (ingreso > 2500000) and (eC == "S") and (uR == "U"):
    print("APROBADO")

elif (ingreso > 3500000) and (aP > 5):
    print("APROBADO")

elif (uR == "R") and (eC == "C") and (nH<2):
    print("APROBADO")

else:
    print("Rechazado")      