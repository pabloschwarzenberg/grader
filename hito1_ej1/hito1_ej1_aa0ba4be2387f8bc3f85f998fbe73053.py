#Nota final
PT = float(input(""))
PI = float(input("Interrogaciones: "))
NE = float(input("Examen: "))
PP = float(input("Presentación: "))

prome = (0.3 * PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print(round(prome, 1))
