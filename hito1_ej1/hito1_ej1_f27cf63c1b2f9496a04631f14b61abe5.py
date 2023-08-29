#Nota final
pt= eval(input("ingrese su nota de tareas: "))
pi= eval(input("ingrese su nota de interrogaciones: "))
ne= eval(input("ingrese su nota del examen: "))
pp= eval(input("ingrese su nota de presentacion: "))
pr=0.3*pt+0.3*pi+0.3*ne+0.1*pp
pr2=round(pr,1)
print("tu promedio es: ",pr2)
