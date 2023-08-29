#Nota final
pt = float(input("Ingrese nota tareas: "))
pi = float(input("Ingrese nota interrogaciones: "))
ne = float(input("Ingrese nota examen: "))
pp = float(input("Ingrese nota presentación: "))

n1 = 30*pt/100
n2 = 30*pi/100
n3 = 30*ne/100
n4 = 10*pp/100

promedio = (n1+n2+n3+n4)
print("La nota final es : ",round(promedio))