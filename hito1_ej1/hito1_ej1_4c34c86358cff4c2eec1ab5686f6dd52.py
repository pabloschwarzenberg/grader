#Nota final
PT = eval(input('ingrese la nota de la tarea :'))
PI = eval(input('ingrese la nota de las interrogaciones :'))
NE = eval(input('ingrese la nota de el examen :'))
PP = eval(input('ingrese la nota de la presentacion :'))
PT = float(PT)
PI = float(PI)
NE = float(NE)
PP = float(PP)
promedio =round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1)
print(promedio)