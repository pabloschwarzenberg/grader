# Aprobación de créditos
# Solicitar datos al cliente
ingreso = int(input('Ingrese su ingreso mensual en pesos: '))
año_de_nacimiento = int(input('Ingrese su año de nacimiento: '))
numero_de_hijos = int(input('Ingrese el número de hijos: '))
años_de_pertenencia = int(input('Ingrese los años de pertenencia al banco: '))
estado_civil = input('Ingrese su estado civil (S para soltero, C para casado): ')
ubicacion = input('Ingrese su ubicación (U para urbano, R para rural): ')

# Evaluar la aprobación del crédito
aprobado = False

if años_de_pertenencia > 10 and numero_de_hijos >= 2:
    aprobado = True

elif estado_civil == 'C' and numero_de_hijos > 3 and 45 <= (2023 - año_de_nacimiento) <= 55:
    aprobado = True

elif ingreso > 2500000 and estado_civil == 'S' and ubicacion == 'U':
    aprobado = True

elif ingreso > 3500000 and años_de_pertenencia > 5:
    aprobado = True

elif ubicacion == 'R' and estado_civil == 'C' and numero_de_hijos < 2:
    aprobado = True

# Imprimir el resultado
if aprobado:
    print('APROBADO')
else:
    print('RECHAZADO')

     