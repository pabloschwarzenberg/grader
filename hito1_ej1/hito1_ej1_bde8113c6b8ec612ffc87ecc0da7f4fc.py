#Nota final
pt=float(input("Ingresa tu nota de tareas: "))
pi=float(input("Ingresa tu nota de interrogación: "))
ne=float(input("Ingresa tu nota de exámen: "))
pp=float(input("Ingresa tu nota de presentación: "))

prom=0.3*pt+0.3*pi+0.3*ne+0.1*pp

print("Tu promedio es de:",round(prom, 1))