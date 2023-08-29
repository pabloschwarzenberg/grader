#Aprobación de créditos
ingreso=int(input("Ingresos en pesos: "))
nacimiento=int(input("año de nacimiemto: "))
edad=2020-nacimiento
hijos=int(input("numero de hijos: "))
años_banco=int(input("Años de pertenencia al banco: "))
estado_civil=input("coloque si es (s)soltero o (c)casado: ")
S= estado_civil
C= estado_civil
vivienda=input("zona donde vive, zona (u)urbana o (R)rural: ")
u=vivienda
r=vivienda
if(años_banco>10) and (hijos>=2):
    print("APROBADO")
elif(estado_civil==c) and (hijos>=3) and (45<=edad<=55):
    print("APROBADO")
elif(ingreso>2500000) and (estado_civil==S) and (vivienda==U):
    print("APROBADO")
elif(ingreso>3500000) and (años_banco>5):
    print("APROBADO")
elif(vivienda==r) and (estado_civil==C) and (hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO") 