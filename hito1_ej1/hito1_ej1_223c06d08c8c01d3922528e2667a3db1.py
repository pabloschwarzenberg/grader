#Nota final
PT = float(input("Ingrese su nota de tareas: "))
PI = float(input("Ingrese su nota de interrogaciones: "))
NE = float(input("Ingrese su nota de Examen: "))
PP = float(input("Ingrese su nota de presentacion: "))
RE = ((PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1))
print("El resultado de tus notas es {0}".format(round(RE,1)))