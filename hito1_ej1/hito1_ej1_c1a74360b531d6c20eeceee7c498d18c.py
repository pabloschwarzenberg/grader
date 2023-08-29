#Nota final
PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogacciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de la presentación: "))

# Calculo
desa = (PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1)

# Resultado
print(round(desa, 1))