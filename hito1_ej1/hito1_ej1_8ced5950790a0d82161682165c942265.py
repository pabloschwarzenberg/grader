#Nota final
pt= float(input("ingrese la nota de sus tareas: "))
pi= float(input("ingrese las notas de sus interrogaciones: "))
ne= float(input("ingrese la nota de su examen: "))
pp= float(input("ingrese la nota de su presentacion: "))
promedio= (0.3*pt+0.3*pi+0.3*ne+0.1*pp)
print("su promedio es: ",round(promedio,1))