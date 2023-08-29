#Nota final
pt= eval(input("Ingrese nota de las tareas:"))
pi= eval(input("Ingrese nota de las investigaciones:"))
ne= eval(input("Ingrese nota de los examenes:"))
pp= eval(input("Ingrese nota de la presentacion:"))
promedio= (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
print("{0:.1f}".format(promedio))