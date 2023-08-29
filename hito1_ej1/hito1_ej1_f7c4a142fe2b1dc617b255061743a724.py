print("ingrese notas en decimales")
a=float(input("nota tarea:"))
x=float(input("nota interrogación:"))
y=float(input("nota examen:"))
z=float(input("nota presentación:"))
pt=a*0.3
pi=x*0.3
ne=y*0.3
pp=z*0.1
total=(pt+pi+ne+pp)
promedio=float(total)
print(promedio)