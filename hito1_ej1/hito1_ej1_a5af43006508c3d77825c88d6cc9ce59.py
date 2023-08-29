#Nota final
pt = float(input("Nota de tareas: "))
pi = float(input("Nota de interrogaciones: "))
ne = float(input("Nota de examen: "))
pp = float(input("Nota de presentacion: "))
f = round(0.3*pt+0.3*pi+0.3*ne+0.1*pp,1)
print(f)