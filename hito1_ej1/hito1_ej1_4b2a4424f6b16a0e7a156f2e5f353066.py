#Nota final
print('\nCalculadora promedio de notas\n')
try:
    PT = float(input('Introduzca las notas de Tareas: '))
    PI = float(input('Introduzca las notas de Interrogaciones: '))
    NE = float(input('Introduzca las notas de Exámenes: '))
    PP = float(input('Introduzca las notas de Presentaciones: '))

    promedio = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)

    print('El promedio de las notas es: ''{:.1f}'.format(promedio))
except:
    print('Sólo números')
      