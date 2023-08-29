#Nota final
PT = float(input("Ingrese tareas: "))
PI = float(input("Ingrese interrogaciones: "))
NE = float(input("Ingrese examenes: "))
PP = float(input("Ingrese presentaciones: "))

pt, pi, ne, pp = float(0.3 * PT), float(0.3 * PI), float(0.3 * NE), float(0.1 * PP)

a = (round(pt + pi + ne + pp,1))
print("promedio final de notas: {}". format(float(a)))