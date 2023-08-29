#Nota final

print('Ingese las notas requeridas para calcular su promedio final:')

PT = float(input('Tareas:\n'))
PI = float(input('Interrogaciones\n'))
NE= float(input('Examen\n'))
PP = float(input('Presentacion\n'))

calculo_promedio = round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP), 1)

print('Su promedio final es de:', calculo_promedio)