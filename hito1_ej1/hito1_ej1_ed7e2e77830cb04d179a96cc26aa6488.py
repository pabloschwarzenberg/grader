#Realiza un programa para preguntar al usuario cuatro notas: PT = Tareas, PI = Interrogaciones, NE= Examen, PP = Presentacion. Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP. Imprime el resultado redondeado a un decimal.
PT=float(input("Nota de Tareas: "))
PI=float(input("Nota de Interrogaciones: "))
NE=float(input("Nota de Examen: "))
PP=float(input("Nota de Presentación: "))
promedio=round((0.3*PT+0.3*PI+0.3*NE+0.1*PP),1)
print("La nota final es de: ",promedio)