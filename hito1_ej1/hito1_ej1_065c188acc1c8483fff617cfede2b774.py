pt = float(input("Ingrese nota tareas: "))
pi = float(input("Ingrese nota interrogaciones: "))
ne = float(input("Ingrese nota examen: "))
pp = float(input("Ingrese nota presentaciones: "))

promedio = (pt *0.3) + (pi * 0.3) + (ne * 0.3) + (pp * 0.1)
print("El promedio final es: ", round(promedio,1))
      