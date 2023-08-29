#Nota final
nota_pt = float(input("ingresa la nota de tareas: "))
nota_pi = float(input("ingresa la nota de interrogaciones: "))
nota_ne = float(input("ingresa la nota de examen: "))
nota_pp = float(input("ingresa la nota de presentación: "))

promedio =  ((0.3 * nota_pt) + (0.3 * nota_pi) + (0.3 * nota_ne) + (0.1 * nota_pp))

print(round (promedio , 1))
