#Nota final
pt = float(input("Tareas: "))
pi = float(input("Interrogaciones: "))
ne = float(input("Examenes: "))
pp = float(input("Presentaciones: "))

pf = (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
print("Promedio Final: ", round(pf,1))
