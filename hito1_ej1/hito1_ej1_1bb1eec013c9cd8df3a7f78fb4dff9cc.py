#Nota final
T = float(input("Ingrese nota Tareas: "))
I = float(input("Ingrese nota Interrogaciones: "))
E = float(input("Ingrese nota Examen: "))
P = float(input("Ingrese nota Presentación: "))
N = (0.3*T)+(0.3*I)+(0.3*E)+(0.1*P)

print("Su nota final es:", round(N,1))      