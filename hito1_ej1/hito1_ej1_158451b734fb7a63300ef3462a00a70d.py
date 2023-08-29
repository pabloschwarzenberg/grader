#Nota final
PT = float(input("Ingresa tu nota de tareas: "))
PI = float(input("Ingresa tu nota de interrogaciones: "))
NE = float(input("Ingresa tu nota de examen: "))
PP = float(input("Ingresa tu nota de presentación: "))
a = 0.3 * PT
b = 0.3 * PI
c = 0.3 * NE
d = 0.1 * PP
prom = (a + b + c + d)
print(round(prom,1))