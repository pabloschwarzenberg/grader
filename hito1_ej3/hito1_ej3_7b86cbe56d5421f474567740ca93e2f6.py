#Aprobación de créditos
ingreso = int(input('Ingreso: '))
nacimiento = eval(input('Ingresa tu año de nacimiento: '))
edad = 2021 - nacimiento
hijos = int(input('Hijos: '))
añobanco = int(input('Banco: '))
civil = str(input('Estado civil S/C: '))
casa = str(input('Urbano o rural U/R: '))
Aprobado = True
Rechazado = False
Credito = True or False

if añobanco >= 10 and hijos >= 2:
    Credito = True
    print ('APROBADO')
elif civil == 'C' and hijos > 3 and edad > 45 and edad < 55:
    Credito = True
    print ('APROBADO')
elif ingreso > 2500000 and civil == 'S' and casa == 'U':
    Credito = True
    print ('APROBADO')
elif ingreso > 3500000 and añobanco > 5:
    Credito = True
    print ('APROBADO')
elif casa == 'R' and civil == 'C' and hijos < 2:
    Credito = True
    print ('APROBADO')
else:
    Credito = False
    print ('RECHAZADO.')