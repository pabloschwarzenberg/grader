#Aprobación de créditos
print('Por favor ingrese sus datos: ')
ingreso=int(input('Ingreso(en pesos): '))
anio=int(input('Año de Nacimiento: '))
edad = 2020 - anio
hijo=int(input('Numero de hijos: '))
pertenencia=int(input('Años de pertenencia al banco: '))
estado=str(input('Estado civil ("S": soltero, "C", casado): '))
sector=str(input('Vive en una ciudad "U" o en zona mas rural "R": '))
if pertenencia>10 and hijo>=2:
    print('APROBADO')
if estado=='C' and hijo>=3 and 45<=edad<=55:
    print('APROBADO')
if ingreso>2500000 and estado=='S' and sector=='U':
    print('APROBADO')
if ingreso>3500000 and pertenencia>5:
    print('APROBADO')
if sector=='R' and estado=='C' and hijo<2:
    print('APROBADO')