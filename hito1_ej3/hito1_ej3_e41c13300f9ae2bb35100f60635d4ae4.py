#Aprobación de créditos
dinero = int(input("ingrese monto de sueldo: "))
añonacimiento = int(input("ingrese año de nacimiento: "))
nhijos = int(input("ingrese numero de hijos: "))
añobanco = int(input("ingrese numero de años perteneciendo al banco: "))
estadocivil = str(input("ingrese estado civil (S, si es soltero)(C, si es casado): "))
vivienda = str(input("ingrese lugar donde vive(U, si vive en zona urbana),(R, si vive en zona rural):"))

if (añobanco>10) and (nhijos>=2):
    print("APROBADO")
elif (estadocivil == "C")and(nhijos>3)and(55<=2021-añonacimiento>=45):
    print("APROBADO")
elif (dinero>=2500000)and(estadocivil=="S")and(vivienda=="U"):
    print("APROBADO")
elif (dinero>=3500000)and(añobanco>5):
    print("APROBADO")
elif (vivienda == "R")and(estadocivil=="C")and(nhijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")
    