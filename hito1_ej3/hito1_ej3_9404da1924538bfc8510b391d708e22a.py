ingresos= int(input("Ingrese los ingresos: ",))
anona= int(input("Ingrese año de nacimiento: ",))
hijos= int(input("Ingrese numero de hijos: ",))
anobanco= int(input("Ingrese los años de pertenencia al banco: ",))
estado=(input("Ingrese S si es soltero y C si es casado: ",))
vive= (input("Ingrese U si vive en urbano y R si rural: ",))
anos=2020-anona
if anobanco>10:
    if hijos>=2:
        print("APROBADO")
if estado=="C":
    if hijos>3:
        if anos>=45 and anos<=55:
            print("APROBADO")
if ingresos>2500000:
    if estado=="S":
        if vive=="U":
            print("APROBADO")
if ingresos>3500000:
    if anobanco>5:
        print("APROBADO")
if vive=="R":
    if estado=="C":
        if hijos<2:
            print("APROBADO")
else:
    print("RECHAZADO")
