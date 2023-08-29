ingreso = int(input('Ingreso: '))
ano_nacimiento = int(input('Año de nacimiento: '))
numero_hijos = int(input('Numero de hijos: '))
anos_banco = int(input('Miembro del banco desde: '))
estado_civil = input('"S": soltero, "C": casado')
lugar_vivienda = input('"U": urbano, "R": rural')
aprobado = False

if anos_banco > 10 and numero_hijos >= 2:
    aprobado = True
elif estado_civil == 'C' and numero_hijos > 3 and 1966 <= ano_nacimiento <= 1976:
    aprobado = True
elif ingreso > 2500000 and estado_civil == 'S' and lugar_vivienda == 'U':
    aprobado = True
elif ingreso > 3500000 and anos_banco > 5:
    aprobado = True
elif lugar_vivienda == 'R' and estado_civil == 'C' and numero_hijos < 2:
    aprobado = True

if aprobado:
    print('APROBADO')
else:
    print('REPROBADO')
