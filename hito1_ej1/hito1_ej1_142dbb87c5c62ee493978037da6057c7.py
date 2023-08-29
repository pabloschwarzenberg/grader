#Nota final
PT = eval(input('ingresa nota de tareas:'))
PI = eval(input('ingresa nota de interrogaciones:'))
NE = eval(input('ingresa nota de examen:'))
PP = eval(input('ingresa nota de presentacion:'))

formula = (float((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)))

print("{:.1f}".format(formula))