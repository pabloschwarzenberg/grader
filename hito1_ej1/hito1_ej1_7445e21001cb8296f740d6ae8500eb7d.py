#Nota final

pt = float(input("ingrese su nota de las tareas "))
pi = float(input("ingrese su nota de las interrogaciones "))
ne = float(input("ingrese su nota de examen "))
pp = float(input("ingrese su nota de las presentaciones "))

promedio = (pt * 0.3) + (pi * 0.3) + (ne * 0.3) + (pp * 0.1)

print(round(promedio, 1))