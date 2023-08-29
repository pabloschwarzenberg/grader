#Aprobación de créditos
from datetime import date
today = date.today()

print('Ingrese los siguientes datos por favor')

ingreso = int(input('Ingreso: '))
fnac = int(input('Año de nacimiento: '))
edad = (int(format(today.year))-int(fnac))
hijos = int(input('Numero de hijos: '))
anosbanco = int(input('Años perteneciente al banco: '))
print('Eliga: "S" si es soltero, "C" si es casado')
ecivil = str(input('Estado civil: '))
print('Eliga: "U" urbano, "R" rural')
vive = str(input('Vive en campo o ciudad: '))

if anosbanco > 10 and hijos >= 2:
    print('APROBADO')
elif ecivil == 'C' and hijos > 3 and 45 <= edad <= 55:
    print('APROBADO')
elif ingreso > 2500000 and ecivil == 'S' and vive == 'U':
    print('APROBADO')
elif ingreso > 3500000 and anosbanco > 5:
    print('APROBADO')
elif vive == 'R' and ecivil == 'C' and hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')