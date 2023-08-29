#Aprobación de créditos
ingreso=int(input("Ingreso: "))
nacimiento=int(input("Año de nacimiento: "))
hijos=int(input("Número de hijos: "))
banco=int(input("Años de pertenencia al banco: "))
civil=str(input("Estado civil: "))
vive=str(input("Vive en: "))
if banco>10 and hijos>=2:
    print("APROBADO")
elif civil=='C' and hijos>3 and 1967<=nacimiento<=1977:
    print("APROBADO")
elif ingreso>2500000 and civil=='S' and vive=='U':
    print("APROBADO")
elif ingreso>3500000 and banco>5:
    print("APROBADO")
elif vive=='R' and civil=='C' and hijos<2:
    print("APROBADO")
else:
    print ("RECHAZADO")















