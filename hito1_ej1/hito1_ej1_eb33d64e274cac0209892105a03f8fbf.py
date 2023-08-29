#Nota final
pt=float(input("Ingresa nota de tareas"))
pi=float(input("Ingresa nota de interrogaciones"))
ne=float(input("Ingresa nota de examen"))
pp=float(input("Ingresa nota de presentacion"))

promedio=round(pt*0.3 + pi*0.3 + ne*0.3 + pp*0.1,1)
print("El promedio es: ", promedio)