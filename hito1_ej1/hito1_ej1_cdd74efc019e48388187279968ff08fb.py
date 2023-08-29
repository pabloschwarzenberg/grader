#Nota final
pt=float(input("inserte su promedio de tareas"))
pi=float(input("inserte su promedio de interrogaciónes"))
ne=float(input("inserte su nota de examen"))
pp=float(input("inserte su nota de presentacion"))
pf=float(0.3*pt+0.3*pi+0.3*ne+0.1*pp)
print("su nota final es", round(pf,1))

