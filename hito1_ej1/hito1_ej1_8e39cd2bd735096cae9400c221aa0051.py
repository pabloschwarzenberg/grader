#Nota final
print("ingrese sus notas para sacar el promedio")
PT = float(input("ingrese tu nota de tarea: "))
PI = float(input("ingrese su nota de interrogaciones: "))
NE = float(input("ingrese su nota de examen: "))
PP = float(input("ingrese su nota de presentacion: "))
promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print (round(promedio,1))
