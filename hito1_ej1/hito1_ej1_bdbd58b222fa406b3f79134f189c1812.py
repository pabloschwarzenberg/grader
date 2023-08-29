#Nota final
PT = eval(input("ingrse la nota de las tareas:") )
PI = eval(input("ingrse la nota de las interrogaciones:")) 
NE = eval(input("ingrse la nota de el examen:") )
PP = eval(input("ingrse la nota de la presentacion:")) 

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
p= round (promedio, 1)

print (p)
