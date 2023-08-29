#Nota final
PT = int(input("ingrese nota de la tareas: ") )
PI = int(input("ingrese nota de la intorrogaciones: "))
NE = int(input("ingrese nota del examen: "))
PP = int(input("ingrese notas de la presentacion: "))

promedio = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print(f"El promedio es igual a {promedio}")