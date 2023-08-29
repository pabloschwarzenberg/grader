#Nota final
# Entradas

pt = float(input("Ingrese su nota de tareas: "))
pi = float(input("Ingrese su nota de interrogaciones: "))
ne = float(input("Ingrese su nota de examen: "))
pp = float(input("Ingrese su nota de presentacion: "))

# Procesamiento
nota_final = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
nota_final = float(round(nota_final, 1))

# Salida
print("Su nota es", nota_final)


      