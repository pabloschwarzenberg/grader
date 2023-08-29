#Aprobación de créditos
ingresos=int(input('ingresos: '))
ano=int(input('ano de nacimiento: '))
hijos=int(input('numero de hijos: '))
banco=int(input('anos de pertenencia al banco: '))
civil=input('estado civil: ')
lugar=input('lugar de residencia: ')
if lugar=='R':
    if civil=='C':
        if hijos<2:
            print('APROBADO')
if banco>10:
    if hijos >=2:
        print('APROBADO')
if civil=='C':
    if hijos>3:
        if ano>= 1965 and ano<=1975:
            print('APROBADO')
if ingresos>250000:
    if civil=='S':
        if lugar=='U':
             print('APROBADO')
if ingresos>350000:
        if banco>5:
            print('APROBADO')
else:
    print('RECHAZADO')
