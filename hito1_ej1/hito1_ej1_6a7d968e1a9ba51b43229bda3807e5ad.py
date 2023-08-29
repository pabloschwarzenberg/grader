#Nota final
print("Introducir notas sin coma, por ejemplo 53")
pt= float(input("Introduce nota de tareas: "))
pi= float(input("Introduce nota de Interrogaciones: "))
ne= float(input("Introduce nota de Examen: "))
pp= float(input("Introduce nota de presentacion: "))

nfinal= (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

print("EL promedio final de semestre es: ", round(nfinal,1))