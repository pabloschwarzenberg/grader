#Nota fin
PT = float(input(" ingrese su nota de tareas: "))
PI = float(input(" ingrese su nota de interrogaciones: "))
NE = float(input(" ingrese su nota de examen: "))
PP = float(input(" ingrese su nota de presentacion: "))
#calculo promedio final 
promedio = round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1)
#salida
print(promedio)