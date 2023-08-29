#nota final
pt=eval(input("ingresar nota de la tarea: "))
pi=eval(input("ingresar nota de interrogaciones: "))
ne=eval(input("ingresar nota de examenes: "))
pp=eval(input("ingresar nota de presentación: "))
pf= round(0.3*pt+0.3*pi+0.3*ne+0.1*pp,1)
print(pf)