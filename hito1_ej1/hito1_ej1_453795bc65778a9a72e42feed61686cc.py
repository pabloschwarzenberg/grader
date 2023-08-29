#Nota final
PT = float(input("ingrese la nota de promedio las tareas: "))
PI = float(input("ingrese la nota de promedio sus interrogaciones: "))
NE = float(input("ingrese la nota de promedio sus exámenes: "))
PP = float(input("ingrese la nota promedio de sus presentaciones: "))
PF = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
print("su promedio final es: ",round(PF,1))