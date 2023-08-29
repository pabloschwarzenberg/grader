#Aprobación de créditos
ingreso = int(input('Ingrese cifra de su ingreso:'))
ano = int(input('Ingrese su año de nacimiento:'))
hijos = int(input('Ingrese la cantidad de hijos:'))
anos_pertenencia = int(input('Ingrese años de pertenencia al banco:'))
estado_civil = str(input('Estado civil:'))
domicilio = str(input('Domicilio:'))
if anos_pertenencia > 10 and hijos >= 2:
    print('APROBADO')
elif estado_civil == 'C' and hijos > 2 and (ano > 45 and ano < 55):
    print('APROBADO')
elif ingreso > 2500000 and estado_civil == 'S' and domicilio =='U':
    print('APROBADO')
elif ingreso > 3500000 and anos_pertenencia > 5:
    print('APROBADO')
elif domicilio == 'R' and estado_civil == 'C' and hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')      