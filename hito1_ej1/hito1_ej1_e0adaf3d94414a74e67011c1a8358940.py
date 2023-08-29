#Nota final


t=float(input("Ingrese nota de Tareas :\n"))
i=float(input("Ingrese nota de Interrogaciones :\n"))
e=float(input("Ingrese nota de Examen :\n"))
p=float(input("Ingrese nota de Presentacion :\n"))

promedio=round((0.3*t)+(0.3*i)+(0.3*e)+(0.1*p), 1)

print(promedio)
      