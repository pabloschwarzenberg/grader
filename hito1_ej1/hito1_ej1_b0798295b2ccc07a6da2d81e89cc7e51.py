#Nota final
PT = float(input("ingresar Nota de tareas: "))
PI = float(input("ingresar Nota de Interrogaciones: " ))
NE = float(input("ingresar Nota de Examen: " ))
PP = float(input("ingresar Nota de examen: " ))

calculo_promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
Nota_final = round(calculo_promedio, 1)
print(Nota_final)