#Nota final
Suma = 0
PT = input("Ingrese nota de Tareas: ")
PI = input("Ingrese nota de Interrogaciones: ")
NE = input("Ingrese nota de Examen: ")
PP = input("Ingrese nota de Presentacion: ")

PT = (float(PT)*0.3)
PI = (float(PI)*0.3)
NE = (float(NE)*0.3)
PP = (float(PP)*0.1)

Suma=PT+PI+NE+PP

print("La nota final es: ",round(Suma, 1))
