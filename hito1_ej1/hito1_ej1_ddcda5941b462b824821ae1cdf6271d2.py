#Nota final
pt=eval(input("Ingrese nota Tarea: "))   
pi=eval(input("Ingrese nota Interrogaciones: "))
ne=eval(input("Ingrese nota Examen: "))
pp=eval(input("Ingrese nota Presentacion: "))
promedio=0.3*pt+0.3*pi+0.3*ne+0.1*pp
print(round(promedio,1))