#Nota final
pt = float(input("ingrese su nota de tareas: "))
pi = float(input("ingrese su nota de interrogaciones: "))
ne = float(input("ingrese su nota de examen: "))
pp = float(input("ingrese su nota de presentacion: "))

promedio = float(0.3)*pt + float(0.3)*pi + float(0.3)*ne + float(0.1)*pp
print("su promedio es", promedio)