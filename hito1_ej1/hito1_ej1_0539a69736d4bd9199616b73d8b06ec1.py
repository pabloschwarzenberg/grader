#Nota final
PT = float(input("Nota de tarea: "))
PI = float(input("Nota de interrogaciones: "))
NE = float(input("Nota de examen: "))
PP = float(input("Nota de presentacion: "))
Calculo = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
print("su promedio es: ", round(Calculo,1))