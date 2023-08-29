#Aprobación de créditosingresos= int(input("Ingrese los ingresos:",))
ingresos= int(input("Ingrese los ingresos:",))
anona= int(input("Ingrese año de nacimiento:",))
hijos= int(input("Ingrese numero de hijos:",))
anobanco= int(input("Ingrese los años de pertenencia al banco:",))
estado=(input("Ingrese C si es casado y S si es soltero:",))
vive=(input("Ingrese R si vive en rural y U si vive en urbano:",))
anos=2020-anona
if anobanco>10 and hijos>=2:
        print("APROBADO")
elif estado=="C" and hijos>3:
    if anos>=45 and anos<=55:
            print("APROBADO")
elif ingresos>2500000 and estado=="S" and vive=="U":
            print("APROBADO")
elif ingresos>3500000 and anobanco>5:
        print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
            print("APROBADO")
else:
    print("RECHAZADO")

    