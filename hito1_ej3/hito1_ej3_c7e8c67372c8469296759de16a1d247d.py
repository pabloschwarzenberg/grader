#Aprobación de créditos
ingreso=int(input("Ingresos (en pesos)"))
anionacimiento=int(input("Año de nacimiento"))
numh=int(input("Número de hijos"))
aniosbanco=int(input("Años de pertenencia al banco"))
estciv=input("Estado civil ('S': soltero, 'C', casado)")
vivienda=input("vive en campo o cuidad ('U': urbano, 'R': rural)")
anios=2021-anionacimiento
if aniosbanco>10 and numh>=2:
    print("APROBADO")
elif estciv=="C" and numh>3 and anios>=45 and anios<=55:
    print("APROBADO")
elif estciv=="S" and ingreso>2500000 and vivienda=="U":
    print("APROBADO")
elif ingreso>3500000 and aniosbanco>5:
    print("APROBADO")
elif vivienda=="R" and estciv=="C" and numh<2:
    print("APROBADO")
else:
    print("RECHAZADO")