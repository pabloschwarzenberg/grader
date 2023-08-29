#Aprobación de créditos
print('Buenos días, para solicitar su crédito debe ingresar los siguientes datos')

ingreso = int(input('Ingreso mensual: $'))
año = int(input('Año de nacimiento: '))
edad = 2017-año
hijos = int(input('Número de hijos:'))
pertenencia = int(input('Años de pertenencia al banco: '))
estado = input('Estado civil (coloque una S si es soltero y una C si esta casado): ')
zona = input('Zona de residencia (si vive en zona urbana coloque una U, si vive en zona rural una R): ')

if pertenencia>10 and hijos>=2:
    print('APROBADO')
elif estado=='C' and hijos>3 and 45<edad<55:
    print('APROBADO')
elif ingreso>3500000 and pertenencia>5:
    print('APROBADO')
elif zona=='R' and estado=='C' and hijos<2:
    print('APROBADO')
else:
    print('RECHAZADO')
