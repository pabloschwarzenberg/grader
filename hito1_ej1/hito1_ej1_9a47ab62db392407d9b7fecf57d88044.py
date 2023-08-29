#Nota final
PT = float(input("ingrese la nota de sus tareas"))
PI = float(input("ingrese nota de interrogaciones"))
NE = float(input("ingrese la nota de su examen"))
PP = float(input("ingrese la nota de presentacion"))
promedio = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("su promedio es :","{:.1f}".format(promedio))