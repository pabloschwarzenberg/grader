#Nota final
pt = float(input("ingrese promedio tareas: "))
pi = float(input("ingrese promedio interrogaciones: "))
ne = float(input("ingrese nota examen: "))
pp = float(input("ingrese puntaje presentación: "))

round(pt)
round(pi)
round(ne)
round(pp)

a = pt * 0.3
b = pi * 0.3
c = ne * 0.3
d = pp * 0.1

suma = a + b + c + d
round(suma)

print("promedio final: {}". format(suma))