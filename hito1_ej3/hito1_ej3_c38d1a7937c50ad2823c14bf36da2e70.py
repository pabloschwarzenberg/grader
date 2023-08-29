#Aprobacion de creditos
ingreso = int(input("Ingrese su ingreso mensual: "))
nacimiento = int(input("Ingrese su ano de nacimiento: "))
hijos = int(input("Ingrese cantidad de hijos: "))
pertenencia = int(input("Ingrese anos de pertenencia al banco: "))
estadocivil = str(input("Ingrese estado civil ('S' soltero, 'C' casado): "))
locacion = str(input("Ingrese si vive en zona urbana (U) o rural (R): "))
if pertenencia > 10 and hijos >= 2:
    print ("APROBADO")
if (estadocivil == 'C') and (hijos > 3) and (1965 < nacimiento < 1975):
    print ("APROBADO")
if ingreso > 2500000 and estadocivil == 'S' and locacion == U:
    print ("APROBADO")
if ingreso > 3500000 and pertenencia > 5:
    print ("APROBADO")
if locacion == 'R' and estadocivil == 'C' and hijos<2:
    print ("APROBADO")
else:
    print ("RECHAZADO")
      