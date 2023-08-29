#Nota final
  # Entradas
pt = float(input("Ingrese nota de tareas: "))
pi = float(input("Ingrese nota de interrogaciones: "))
ne = float(input("Ingrese nota de examen: "))
pp = float(input("Ingrese nota de presentacion: "))

# Procesamiento
a = pt * 0.3
b = pi * 0.3
c = ne * 0.3
d = pp * 0.1

r = round((a + b + c + d), 1)

# Salida
print("Su promedio es: ", r)
      