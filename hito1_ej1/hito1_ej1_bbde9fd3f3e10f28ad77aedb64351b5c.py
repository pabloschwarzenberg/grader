#Nota final
PT = float(input("Ingrese una nota de Tareas: "))
PI = float(input("Ingrese una nota de Interrogaciones: "))
NE = float(input("Ingrese una nota de Examen: "))
PP = float(input("Ingrese una nota de Presentacion: "))

formula = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print("El resultado de la suma de las notas redondeado a un decimal es: ", round(formula,1))