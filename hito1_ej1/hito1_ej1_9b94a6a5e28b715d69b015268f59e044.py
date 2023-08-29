#Nota final
print("ingrese su nota de tareas")
pt = float(input())
print("ingrese su nota de interrogacion")
pi = float(input())
print("ingrese su nota de examen")
ne = float(input())
print("ingrese su nota de presentacion")
pp = float(input())
promedio = pt * 0.30 + pi * 0.30 + ne * 0.30 + pp * 0.10
print("su nota final es: ", round(promedio,1))      