#Nota final
pt=float(input("ingrese la nota de tareas :"))
pi=float(input("ingrese nota de interrogaciones"))
ne=float(input("ingrese nota de examen"))
pp=float(input("ingrese nota de presentacion"))
promedio=(0.3*pt+0.3*pi+0.3*ne+0.1*pp)
promedio=round(promedio,2)
print(promedio)