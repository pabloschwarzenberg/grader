#Nota final
PT = float(input('Ingrese las notas de las tareas: '))
PI = float(input('Ingrese las notas de las interrogaciones: '))
NE = float(input('Ingrese las notas de las examenes: '))
PP = float(input('Ingrese las notas de las presentaciones: '))

#FORMULa
calculo = 0.3 * (PT) + 0.3 *(PI) + 0.3 * (NE) + 0.1 * PP

#Resultado

print('El promedio final es: ', round(calculo, 1))