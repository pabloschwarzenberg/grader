#Nota final

PT = float(input('Ingrese su nota de tareas de forma decimal: '))
PI = float(input('Ingrese su nota interrogaciones de forma decimal: '))
NE = float(input('Ingrese su nota de exámen de forma decimal: '))
PP = float(input('Ingrese su nota de presentación de forma decimal: '))

promedio = float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print('Su promedio es:', round(promedio, 1))