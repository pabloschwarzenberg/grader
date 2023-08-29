#Nota final
print("ingrese nota tareas  ")
pt = float(input(""))     
print("ingrese nota interrogaciones  ")
pi = float(input(""))
print("ingrese nota examen  ")
ne = float(input(""))
print("ingrese nota presentacion  ")
pp = float(input(""))

suma = ((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp))


print(round(suma, 1))