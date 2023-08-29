PT = float(input("Ingrese su nota de (Tarea): "))
PL = float(input("Ingrese su nota de (Interrogación): "))
NE = float(input("Ingrese su nota de (Examen): "))
PP = float(input("Ingrese su nota de (Presentación): "))

x = (0.3 * PT) + (0.3 * PL) + (0.3 * NE) + (0.1 * PP)
promedio_final = round(x, 1)

print(promedio_final)




