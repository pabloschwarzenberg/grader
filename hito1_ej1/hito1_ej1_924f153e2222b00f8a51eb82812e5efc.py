#Nota final
PT = float(input("ingrese su nota de tarea:"))
PI = float(input("ingrese su nota de interrogaciones:"))
NE = float(input("ingrese su nota de examen:"))
PP = float(input("ingrese su nota de presentacion:"))

PROMEDIO = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print (round(PROMEDIO,1))
     