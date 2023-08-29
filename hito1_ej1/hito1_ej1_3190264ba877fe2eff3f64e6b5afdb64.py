#Nota final
pt = float(input("Digame la nota de sus tareas: "))
pi = float(input("Digame la nota de sus interrogaciones: "))
ne = float(input("Digame la nota de sus examenes: "))
pp = float(input("Digame la nota de sus presentaciones: "))
pt2 = pt / 10
pt3 = pt2 * 3
pi2 = pi / 10
pi3 = pi2 * 3
ne2 = ne / 10
ne3 = ne2 * 3
pp2 = pp / 10
promedio = pt3 + pi3 + ne3 + pp2
if promedio % 2 != 0:
  promedio = promedio + 1
print("Su promedio de notas es: ", (promedio))