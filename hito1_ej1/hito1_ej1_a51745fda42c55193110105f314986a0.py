#Nota final

PT = float(input("Ingrese Nota Tareas "))
PI = float(input("Ingrese Nota Interrogaciones "))
NE = float(input("Ingrese Nota Examen "))
PP = float(input("Ingrese Nota Presentacion "))

PF = round((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP), 1)

print("El Promedio Final es ", PF)

      