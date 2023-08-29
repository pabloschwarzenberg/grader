#Aprobación de créditos
ingresos=int(input("Ingresos: "))
año=int(input("Año de nacimiento: "))
hijos=int(input("Número de hijos: "))
banco=int(input("Años de pertenencia al banco: "))
civil=input("Estado civil: ")
residencia=input("Lugar de residencia: ")
if residencia=='R':
    if civil=='C':
        if hijos<2:
            print('APROBADO')
if banco>10:
    if hijos >=2:
        print('APROBADO')
if civil=='C':
    if hijos>3:
        if año>= 1965 and año<=1975:
            print('APROBADO')
if ingresos>250000:
    if civil=='S':
        if residencia=='U':
             print('APROBADO')
if ingresos>350000:
        if banco>5:
            print('APROBADO')
else:
    print('RECHAZADO')