PT = eval(input('Ingrese nota de Tarea :'))
PI = eval(input('Ingrese nota de Interrrogacion :'))
NE = eval(input('Ingrese Nota de Examen :'))
PP = eval(input('Ingrese Nota de Presentacion :'))
Promedio = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print('Su Promedio es : ' , round(Promedio, 1))