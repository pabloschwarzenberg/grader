#Nota final

Tareas = eval(input('ingresar nota: '))

Interrogaciones = eval(input('ingresar nota: '))

Examen = eval(input('ingresar nota: '))

Presentacion = eval(input('ingresar nota: '))

 

PT=Tareas

PI=Interrogaciones

NE=Examen

PP=Presentacion
 
FormulaX=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
FormulaZ=(round(FormulaX,1))


print('nota final: ', FormulaZ)
