PT = eval(input("Ingrese su nota de tareas: "))
PI = eval(input("Ingrese su nota de interrogaciones: "))
NE = eval(input("Ingrese su nota de examen: "))
PP = eval(input("Ingrese su nota de presentaión: "))
promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE +0.1 * PP
promedio1 = round(promedio,1)
print(promedio1)