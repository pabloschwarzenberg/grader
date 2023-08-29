#Nota final
pt= eval(input('ingrese nota tarea: '))
pi= eval(input('ingrese nota interrogaciones: '))
ne= eval(input('ingrese nota examen: '))
pp= eval(input('ingrese nota presentacion: '))

x=(0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp)
print(round(x,1))     