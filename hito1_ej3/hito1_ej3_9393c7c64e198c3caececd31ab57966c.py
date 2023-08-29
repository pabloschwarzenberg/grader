#Aprobación de créditos
ing = int(input('Indique su ingreso:'))
year = int(input('Indique su año de nacimiento:'))
hijos = int(input('Cuántos hijos tiene:'))
yearb = int(input('Cuánto años tiene como cliente en el banco:'))
strE = input('Digite "S" si es soltero o "C"si es casado:')
strV = input('Digite "U" si su domicilio es urbano o "R" si es rural:')
if yearb > 10 and hijos >= 2:
    print('APROBADO')
elif strE.upper() == 'C' and hijos > 3 and 45 < 2023-year < 55:
    print('APROBADO')
elif ing > 2500000 and strE.upper() == 'S' and strV.upper() == 'U':
    print('APROBADO')
elif ing > 3500000 and yearb > 5:
    print('APROBADO')
elif strV.upper() == 'R' and strE.upper() == 'C' and hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')      