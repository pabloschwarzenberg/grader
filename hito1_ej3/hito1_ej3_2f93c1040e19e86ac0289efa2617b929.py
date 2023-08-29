ingresos = int(input('Ingreso: '))
nacimiento = eval(input('Ingresa tu año de nacimiento: '))
edad = 2021 - nacimiento
hijos = int(input('Hijos: '))
añobanco = int(input('Banco: '))
estado = str(input('Estado civil S/C: '))
vivienda = str(input('Urbano o rural U/R: '))
Aprobado = True
Rechazado = False
Credito = True or False

if añobanco >= 10 and hijos >= 2:
    Credito = True
    print ('APROBADO')
elif estado == 'C' and hijos > 3 and edad > 45 and edad < 55:
    Credito = True
    print ('APROBADO')
elif ingresos > 2500000 and estado == 'S' and vivienda == 'U':
    Credito = True
    print ('APROBADO')
elif ingresos > 3500000 and añob > 5:
    Credito = True
    print ('APROBADO')
elif vivienda == 'R' and estado == 'C' and hijos < 2:
    Credito = True
    print ('APROBADO')
else:
    Credito = False
    print ('RECHAZADO.')