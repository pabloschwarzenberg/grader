#Nota final
pt=eval(input("Ingrese nota de tarea: "))
pi=eval(input("Ingrese nota de Interrogaciones: "))
ne=eval(input("Ingrese nota de Examen: "))
pp=eval(input("Ingrese nota de Presentación: "))

promedioFinal=(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)

print(round(promedioFinal,1))     