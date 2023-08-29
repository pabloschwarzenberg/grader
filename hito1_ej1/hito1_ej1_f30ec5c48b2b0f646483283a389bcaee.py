#Nota final
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion




PT = eval(input ("nota tareas"))
PI = eval(input("nota interrogaciones"))
NE = eval(input("nota examen"))
PP = eval(input("nota presentacion"))
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
print("su promedio es: ", round(promedio,1))