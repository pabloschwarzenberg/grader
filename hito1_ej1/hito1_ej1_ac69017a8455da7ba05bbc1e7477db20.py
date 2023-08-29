#Nota final
pt = float(input("Nota de sus Tareas: "))
pi = float(input("Nota de sus Interrogaciones: "))
ne = float(input("Nota de sus Examen: "))
pp = float(input("Nota de Presentación: "))

n1 = 0.3*pt
n2 = 0.3*pi
n3 = 0.3*ne
n4 = 0.1*pp

suma = n1+n2+n3+n4
print(round(suma,1))
