#Nota final
pt=eval(input("Ingrese nota de tareas: "))
pi=eval(input("Ingrese nota de interrogaciones: "))
ne=eval(input("Ingrese nota de exámen: "))
pp=eval(input("Ingrese nota de presentación: "))
promedio=0.3*pt+0.3*pi+0.3*ne+0.1*pp
x=round(promedio,1)
print("Su promedio final es",x)      