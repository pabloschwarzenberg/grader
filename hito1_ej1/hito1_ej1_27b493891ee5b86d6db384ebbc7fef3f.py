#Nota final
PT = float(input("Ingrese la nota de tareas (PT): "))
PI = float(input("Ingrese la nota de interrogaciones (PI): "))
NE = float(input("Ingrese la nota del exámen (NE): "))
PP = float(input("Ingrese la nota de presentación (PP): "))

promediofinal = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(promediofinal,1))