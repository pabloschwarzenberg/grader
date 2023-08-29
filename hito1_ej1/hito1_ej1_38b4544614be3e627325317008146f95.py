#Nota final
pt = float(input("Ingrese su nota de Tareas: "))
pi = float(input("Ingrese su nota de Interrogaciones: "))
ne = float(input("Ingrese su nota de Examen: "))
pp = float(input("Ingrese su nota de Presentación: "))

ptend = pt * 0.3
piend = pi * 0.3
neend = ne * 0.3
ppend = pp * 0.1
resultado = ptend + piend + neend + ppend
print (resultado)