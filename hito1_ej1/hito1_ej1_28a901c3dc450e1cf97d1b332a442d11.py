#Nota final
PT= eval(input(' Ingresa tu nota de tareas: '))
PI= eval(input(' Ingresa tu nota de interrogaciones: '))
NE= eval(input(' Ingresa tu nota de examen: '))
PP= eval(input(' Ingresa tu nota de presentacion: '))

formula=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print(float(formula))

