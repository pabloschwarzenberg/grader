#Aprobación de créditos
print('** APROBACIÓN DE CRÉDITOS **')
ingreso = int(input())
nacimiento = int(input())
hijos = int(input())
pertenencia = int(input())
estado = input()
vivienda = input()

if pertenencia > 10:
    if hijos >= 2:
        print('APROBADO')
    else:
        print('RECHAZADO')
if estado == 'C':
    if hijos > 3:
        if (nacimiento >= 1961) and (nacimiento <= 1971): #Año actial 2016
            print('APROBADO')
        else:
            print('RECHAZADO')
    else:
        print('RECHAZADO')
if ingreso > 2500000:
    if estado == 'S':
        if vivienda == 'U':
            print('APROBADO')
        else:
            print('RECHAZADO')
    else:
        print('RECHAZADO')
if ingreso > 3500000:
    if pertenencia > 5:
        print('APROBADO')
    else:
        print('RECHAZADO')
if vivienda == 'R':
    if estado == 'C':
        if hijos < 2:
            print('APROBADO')
        else:
            print('RECHAZADO')
    else:
        print('RECHAZADO')
else:
    print('RECHAZADO')