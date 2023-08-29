#Nota final
PT=float(input("Ingresar notas de tareas:"))
PI=float(input("Ingresar notas de interrogaciones:"))
NE=float(input("ingresar notas de examen:"))
PP=float(input("Ingresar notas de presentaciones:"))

prom = (0.3*(PT)+0.3*(PI)+0.3*(NE)+0.1*(PP))
print("El Promedio Es:" ,round(prom,1),)     