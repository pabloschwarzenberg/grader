#Aprobación de créditos
s = int(input('sueldo: '))
a = eval(input('ingresa tu año de nacimiento: '))
edad = 2021 - a
h = int(input('numero de hijos: '))
ab = int(input('años en el banco: '))
e = str(input('Estado civil S/C: '))
v = str(input('Urbano o rural U/R: '))
Aprobado = True
Rechazado = False
Credito = True or False

if ab >= 10 and h >= 2:
    Credito = True
    print ('APROBADO')
elif e == 'C' and h > 3 and edad > 45 and edad < 55:
    Credito = True
    print ('APROBADO')
elif s > 2500000 and e == 'S' and v == 'U':
    Credito = True
    print ('APROBADO')
elif s > 3500000 and ab > 5:
    Credito = True
    print ('APROBADO')
elif v == 'R' and e == 'C' and h < 2:
    Credito = True
    print ('APROBADO')
else:
    Credito = False
    print ('RECHAZADO.')