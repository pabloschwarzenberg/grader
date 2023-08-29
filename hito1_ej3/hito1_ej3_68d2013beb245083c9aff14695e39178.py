Ingreso = int(input('Cuales son sus ingresos?:'))
Agno_Nacimiento = int(input('Ingrese año de nacimiento:'))
Numero_hijos = int(input('Ingrese numero de hijos:'))
Agnos_Banco = int(input('Ingrese años de pertenencia al banco:'))
Estado_Civil = str(input('S:Soltero, C:Casado:'))
Residencia = str(input('U:Urbano, R:Rural:'))

Edad = 2020 - Agno_Nacimiento

if Agnos_Banco >= 10 and Numero_hijos >= 2:
    print('APROBADO')
elif Estado_Civil == 'C' and Numero_hijos >= 3 and 45 <= Edad <= 55:
    print('APROBADO')
elif Ingreso >= 2500000 and Estado_Civil == 'S' and Residencia == 'U':
    print('APROBADO')
elif Ingreso >= 3500000 and Agnos_Banco >= 5:
    print('APROBADO')
elif Residencia == 'R' and Estado_Civil == 'C' and Numero_hijos <= 2:
    print('APROBADO')
else:
    print('RECHAZADO')
    