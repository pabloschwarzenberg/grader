#Nota final
pt=eval(input("ingrese su nota de tareas: "))
pi=eval(input("ingrese nota de interrogaciones: "))
ne=eval(input("ingrese su nota de examen: "))
pp=eval(input("ingrese su nota de presentacion: "))
notas=pt+pi+ne
promedio_final=(notas*0.3)+(pp*0.1)
print(round(promedio_final,1))