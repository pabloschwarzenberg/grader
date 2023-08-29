#Aprobación de créditos
Ingreso = int(input("Ingreso : "))
anioNacimiento = int(input("Año de nacimiento: "))
numHijos = int(input("Número de hijos: "))
aniosBanco = int(input("Años de pertenencia al banco: "))
estadoCivil = str(input("Estado civil: "))
campoCiudad = str(input("Si vive en campo o cuidad : "))

edad = 2021 - anioNacimiento

if aniosBanco >= 10 and numHijos >= 2:
    print('APROBADO')
else:
    print('RECHAZADO ')
if estadoCivil == 'C' and numHijos > 3 and edad >= 45 and edad <= 55:
    print('APROBADO')
else:
    print('RECHAZADO ')
if Ingreso > 2500000 and estadoCivil == 'S' and campoCiudad == 'U':
    print('APROBADO')
else:
    print('RECHAZADO ')
if Ingreso > 3500000 and aniosBanco > 5:
    print('APROBADO')
else:
    print('RECHAZADO ')
if campoCiudad == 'R' and estadoCivil == 'C' and numHijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO ')
     