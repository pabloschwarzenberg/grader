print("Realiza un programa para preguntar al usuario cuatro notas:")

print("PT = Tareas")
print("PI = Interrogaciones")
print("NE= Examen")
print("PP = Presentacion")

print("Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP")
print("Imprime el resultado redondeado a un decimal")

PT=float(input("escriba nota tareas: "))
PI=float(input("escriba nota interrogaciones: "))
NE=float(input("escriba nota examen: "))
PP=float(input("escriba nota precentacion: "))

promedio= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("el promedio final es: ",promedio)