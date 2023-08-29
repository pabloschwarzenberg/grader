#Nota final
PT = float(input("Ingrese nota de Tareas: "))
PI = float(input("Ingrese nota de Interrogaciones: "))
NE = float(input("Ingrese nota del Examen: "))
PP = float(input("Ingrese nota de Presentacion: "))
Nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("El resultado redondeado a un decimal es: ", round(Nota_final,1))