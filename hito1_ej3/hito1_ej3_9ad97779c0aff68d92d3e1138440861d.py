#Aprobación de créditos
ingresos=int(input("Monto de ingresos en pesos:"))
nacimiento=int(input("Año de nacimiento:"))
edad=2017-nacimiento
hijos=int(input("Cantidad de hijos:"))
añosbanco=int(input("Años de pertenencia al banco:"))
estadocivil=input("Estado civil: S/C")
vivienda=input("¿Vive en campo o ciuda?: U/R")
if añosbanco>10 and hijos>=2:
                         print("APROBADO")
if estadocivil=="C" and hijos>3 and edad>=45 and edad<=55:
    print("APROBADO")
    
if ingresos>2500000 and estadocivil=="S" and vivienda=="U":
    print("APROBADO")

if ingresos>3500000 and añosbanco>=5:
    print("APROBADO")

if vivienda=="R" and estadocivil=="C" and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")
