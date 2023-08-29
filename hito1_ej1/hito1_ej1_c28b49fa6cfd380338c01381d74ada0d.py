#Nota final
pt=float(input("ingresa nota de tareas:"))
pi=float(input("ingresa nota de interrogaciones:"))
ne=float(input("ingresa nota de examen:"))
pp=float(input("ingresa nota de presentacion:"))
promedio=0.3*pt+0.3*pi+0.3*ne+0.1*pp
print("el promedio final de notas es",round(promedio,1))