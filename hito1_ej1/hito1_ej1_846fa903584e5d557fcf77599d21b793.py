#Nota final
PT = float(input("ingrese su nota de Tareas: "))
PI = float(input("ingrese su nota de Interrogaciones: "))
NE = float(input("ingrese su nota de Examen: ")) 
PP = float(input("ingrese su nota de Presentacion: "))
Promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("su nota final es:", Promedio)
print(round(Promedio, 1))