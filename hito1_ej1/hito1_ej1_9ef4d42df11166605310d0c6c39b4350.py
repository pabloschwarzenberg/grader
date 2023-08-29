PT = float(input("ingrese su nota de (Tarea): "))
PL = float(input("ingrese su nota de (Interogacion): "))
NE = float(input("ingrese su nota de (Examen): "))
PP = float(input("ingrese su nota de (Presentacion): "))

x = (0.3 * PT) + (0.3 * PL) + (0.3 * NE) + (0.1 * PP)
promedio_final = round(x, 1)

print(promedio_final)