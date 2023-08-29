#Nota final
pt= float(input("ingrese nota de tareas: "))
pi= float(input("ingrese nota de interrogacion: "))
ne= float(input("ingrese nota de Examen: "))
pp=float(input("ingrese nota de presentacion: "))

pf =0.3*pt+0.3*pi+0.3*ne+0.1*pp

print(round(pf,1))