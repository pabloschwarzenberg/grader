#Nota final
pt=float(input("Ingrese su nota de tareas:"))
pi=float(input("Ingrese su nota de interrogaciones:"))
ne=float(input("Ingrese su nota examenes:"))
pp=float(input("ingrese su nota de presentacion:"))
promedio=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
promedio=round(promedio,1)
print("el promedio final es",promedio)
     