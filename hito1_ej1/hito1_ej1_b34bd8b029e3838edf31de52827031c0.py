#Nota final
PT =float(input("ingresa tareas: "))
PI =float(input("ingresa interrogaciones: "))
NE=float(input("ingresa examen: "))
PP = float(input("ingresa Presentacion: "))

promedio=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("tu promedio es:",round(promedio, 1))