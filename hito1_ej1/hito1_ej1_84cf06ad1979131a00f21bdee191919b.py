#Realiza un programa para preguntar al usuario cuatro notas:
#PT = Tareas
PT = float(input("Ingrese nota de Tareas: "))
P_denota1 = 0.3*PT
#PI = Interrogaciones
PI = float(input("Ingrese nota de Interrogaciones: "))
P_denota2 = 0.3*PI
#NE= Examen
NE = float(input("Ingrese nota de examen: "))
P_denota3 = 0.3*NE
#PP = Presentacion
PP = float(input("Ingrese nota de Presentación: "))
P_denota4 = 0.1*PP
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP Imprime el resultado redondeado a un decimal.
Promediofinal = (P_denota1+P_denota2+P_denota3+P_denota4)
print("La nota final es de: " , round(Promediofinal , 1))