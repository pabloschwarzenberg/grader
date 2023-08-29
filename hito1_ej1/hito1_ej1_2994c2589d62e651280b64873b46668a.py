#Nota final
PT = eval(input("Ingrese la nota de Tareas:"))
PI = eval(input("Ingrese la nota de Interrogaciones:"))
NE = eval(input("Ingrese la nota de Examen:"))
PP = eval(input("Ingrese la nota de Presentacion:"))
 
promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
 
print(round(promedio,1))