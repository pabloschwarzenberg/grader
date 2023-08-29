#Nota final
PT = float(input("ingrese su nota para Tareas:"))
PI = float(input("ingrese su nota para interrogaciones:"))
NE = float(input("ingrese su nota para examen:"))
PP = float(input("ingrese su nota para Presentacion:"))
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
promedio_final_redondeado = round(promedio_final, 1)
print("su promedio final es",promedio_final_redondeado)