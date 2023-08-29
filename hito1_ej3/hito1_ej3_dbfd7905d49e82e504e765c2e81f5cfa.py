Ingreso = int(input("Ponga aqui su ingresos:"))

Edad = int(input("Ingrese su año de nacimiento:"))

Hijos = int(input("Ingrese aqui su numero de hijos:"))

Pertenencia = int(input("Ingrese aqui sus años de pertenencia en el banco"))

Civil = str(input("Estado civil: S = SOLTERO, C = CASADO"))

Lugar = str(input("Inidique si vive en Ciudad = U o en el Campo = R"))

Año = Edad - 2022

if Pertenencia > 10 and Hijos >= 2:
    print("APROBADO")

elif Civil == "C" and Hijos > 3 and Año > 44 and Año < 56:
    print("APROBADO")

elif Ingreso > 2500000 and Civil == "S" and Lugar == "U":
    print("APROBADO")

elif Ingreso > 3500000 and Pertenencia > 5:
    print("APROBADO")

elif Lugar == "R" and Civil == "C" and Hijos < 3:
    print("APROBADO")

else:
    print("RECHAZADO")
