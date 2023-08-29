#Nota final
pt=eval(input('Ingrese nota TAREAS: '))
pi=eval(input('Ingrese nota INTERROGACIONES: '))
ne=eval(input('Ingrese nota EXAMEN: '))
pp=eval(input('Ingrese nota PRESENTACION: '))
formula=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
h=round(formula,1)
print(h)