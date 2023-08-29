PT= eval(input('ingrese su nota de tarea:'))
PI= eval(input('ingrese su nota de interrogaciones:'))
NE= eval(input('ingrese su nota de examen:'))
PP= eval(input('ingrese su nota de presentacion:'))

NT= float(0.3*PT+ 0.3*PI+ 0.3*NE+ 0.1*PP)

print('su nota final es:',round(NT,1))