#Nota final
pt=eval(input("ingrese nota tareas: "))
pi=eval(input("ingrese nota interrogaciones: "))
ne=eval(input("ingrese nota examen: "))
pp=eval(input("ingrese nota presentación: "))

promedio=0.3*pt+0.3*pi+0.3*ne+0.1*pp

print(round(promedio,1))      