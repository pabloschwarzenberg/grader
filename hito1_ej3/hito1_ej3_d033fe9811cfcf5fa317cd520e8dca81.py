ingreso=int(input("Ingrese cantidad de ingreso: "))
nacimiento=int(input("Ingrese año de nacimiento: "))
cantidadhijos=int(input("Ingrese cantidad de hijos: "))
sociobanco=int(input("Ingrese cantidad de años de pertenencia al banco: "))
estadocivil=input("Ingrese su estado civil: ")
ubicaciondevivienda= input("Ingrese ubicacion de vivienda: ")

if(sociobanco>10 and cantidadhijos>=2):
    print("APROBADO")
else:
        print("REPROBADO")
if(estadocivil=="C" and cantidadhijos>=3 and  nacimiento>=1965):
    print("APROBADO")
else:
        print("REPROBADO")
if(ingreso>2500000 and estadocivil=="S" and ubicaciondevivienda=="U"):
    print("APROBADO")
else:
        print("REPROBADO")
if(ingreso>3500000 and sociobanco>5):
    print("APROBADO")
else:
        print("REPROBADO")
if(ubicaciondevivienda=="R" and estadocivil=="C" and cantidadhijos<2):
    print("APROBADO")
else:
        print("REPROBADO")