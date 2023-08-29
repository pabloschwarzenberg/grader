#Nota final
import decimal 
pregunta = print('Ingrese las notas para consultar su promedio final')
PT = float(input('Ingrese la nota de Tareas: '))
PI = float(input('Ingrese la nota de Interrogaciones: '))
NE = float(input('Ingrese la nota de Examen: '))
PP = float(input('Ingrese la nota de Presentacion: '))

#Operatoria
Promedio = (PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1)

#Salida
print('Su promedio final es: ')
print(round(Promedio, 1))