#Nota final
Tareas = eval(input('ingresa la 1ra nota: '))
Interrogaciones = eval(input('ingresa la 2da nota: '))
Examen = eval(input('ingresa la 3ra nota: '))
Presentacion = eval(input('ingresa la 4ta nota: '))

PT=Tareas
PI=Interrogaciones
NE=Examen
PP=Presentacion

FormulaX=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
FormulaZ=(round(FormulaX,1))

print('tu nota final es: ', FormulaZ)