#Nota final
pt=float(input("ingrese nota de tarea: " ))
pi=float(input("ingrese nota de interrogaciones: " ))
ne=float(input("ingrese nota de examen: " ))
pp=float(input("ingrese nota de presentacion: " ))
nota_final = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
print("nota final del curso es: ", round(nota_final, 1))