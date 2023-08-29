#Nota final
nota_pt = float(input("ingrese nota de tareas: "))
nota_pi = float(input("ingrese nota de interrogaciones: "))
nota_ne = float(input("ingrese nota de examen: "))
nota_pp = float(input("ingrese nota de presentacion: "))

promedio = round(0.3*nota_pt + 0.3*nota_pi + 0.3*nota_ne + 0.1*nota_pp ,1)

print(promedio)