#Aprobación de créditos
ingreso=int(input("Ingrese cantidad de ingreso: "))
nacimiento=int(input("Ingrese año de nacimiento: "))
canthijos=int(input("Ingrese cantidad de hijos: "))
sociobanco=int(input("Ingrese cantidad de años de pertenencia al banco: "))
estadocivil=input("Ingrese su estado civil: ")
lugardevivienda= input("Ingrese lugar de vivienda: ")

if(sociobanco>10 and canthijos>=2):
    print("APROBADO")
else:
        print("REPROBADO")
if(estadocivil=="C" and canthijos>=3 and  nacimiento>=1965):
    print("APROBADO")
else:
        print("REPROBADO")
if(ingreso>2500000 and estadocivil=="S" and lugardevivienda=="U"):
    print("APROBADO")
else:
        print("REPROBADO")
if(ingreso>3500000 and sociobanco>5):
    print("APROBADO")
else:
        print("REPROBADO")
if(lugardevivienda=="R" and estadocivil=="C" and canthijos<2):
    print("APROBADO")
else:
        print("REPROBADO")