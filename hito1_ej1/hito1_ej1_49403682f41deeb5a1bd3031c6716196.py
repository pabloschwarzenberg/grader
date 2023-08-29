#Nota final
print("Por favor menciona tu promedio en los siguentes aspectos")

PT = float(input("Tareas : "))
PI = float(input("Interrogaciones : "))
NE = float(input("Examen: "))
PP = float(input("Presentacion : "))

resultado = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
print (round(resultado , 1))
