#Suma de los N primeros números
n=int(input("Ingresa un número: "))
natural=n*(n+1)/2
print(natural)
#Nota final
pt=float(input("Ingresa tu nota de tareas: "))
pi=float(input("Ingresa tu nota de interrogación: "))
ne=float(input("Ingresa tu nota de exámen: "))
pp=float(input("Ingresa tu nota de presentación: "))

prom=0.3pt+0.3pi+0.3ne+0.1pp

print("Tu promedio es de:",round(prom, 1))
#Nota final
PT = eval(input("Tareas"))
PI = eval(input("Interrogaciones"))
NE = eval(input("Examen"))
PP = eval(input("Presentacion"))

promedio = (0.3 * PT) + (0.3PI) + (0.3NE) + (0.1*PP)
print(promedio)