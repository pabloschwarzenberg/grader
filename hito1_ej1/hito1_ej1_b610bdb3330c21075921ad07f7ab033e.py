#Nota final
# Entrada
PT = float(input("Ingrese la nota de las tareas:"))
PI = float(input("Ingrese la nota de las interrogaciones:"))
NE = float(input("Ingrese la nota del examen:"))
PP = float(input("Ingrese la nota de la presentacion:"))

# Formula
PF =((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
redondeo = "{0:.1f}".format(PF)
# Salida
print("El promedio final es",redondeo.format(PF))