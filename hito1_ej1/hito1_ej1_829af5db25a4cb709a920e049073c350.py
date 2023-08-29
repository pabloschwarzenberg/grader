#entrada
PT = float(input('ingrese las notas de las tareas: '))
PI = float(input('ingrese las notas de las interrogaciones: '))
NE = float(input('ingrese las notas de las examenes: '))
PP = float(input('ingrese las notas de las presentaciones: '))

#procesamiento

Promedio = 0.3 * (PT) + 0.3 * (PI) + 0.3 * (NE) + 0.1 * (PP)
 
#salida
print('el promedio final es: ', Promedio )
