#Nota final
PT = float(input("ingresar nota de tareas:"))
PI = float(input("ingresar nota de interrogaciones:"))
NE = float(input("ingresar nota de examen:"))
PP = float(input("ingresar nota de presentacion:"))

operacion = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
round(operacion,3)
print("su nota de promedio es:",operacion)