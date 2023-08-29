#Nota final
PT = float(input("Ingrese Nota de Tareas: "))
PI = float(input("Ingrese Nota de Interrogaciones: "))
NE = float(input("Ingrese Nota de Exámen: "))
PP = float(input("Ingrese Nota de Presentación: "))

x = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
r = round(x, 1)
print("El promedio es ", r)
      