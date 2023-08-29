#Aprobación de créditos

ingreso=int(input("Ingreso: "))
nacimiento=int(input("Año de nacimiento: "))
hijos=int(input("Número de hijos: "))
anosbanco=int(input("Años de pertenencia al banco: "))
estadocivil=str(input("Estado civil (S o C): "))
dondevive= str(input("Vive en campo o cuidad (U o R): "))

if anosbanco>10 and hijos>=2:
    print("APROBADO")
elif estadocivil== "C" and hijos>=3 and 1963<nacimiento<1973:
    print("APROBADO")
elif ingreso>2500000 and estadocivil=="S" and dondevive== U:
    print("APROBADO")
elif ingreso>3500000 and anosbanco>5:
    print("APROBADO")
elif dondevive=="R" and estadocivil== "C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")