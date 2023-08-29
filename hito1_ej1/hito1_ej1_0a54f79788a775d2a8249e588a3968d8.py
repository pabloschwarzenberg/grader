#Nota final
N1=float(input("Ingrese nota de tareas: "))
N2=float(input("ingresew nota de Interrogaciones: "))
N3=float(input("ingrese nota de Examen: "))
N4=float(input("ingrese nota de Presentacion: "))

PT = 0.3*N1
PI = 0.3*N2
NE = 0.3*N3
PP = 0.1*N4

resultado=PT+PI+NE+PP

print(resultado)