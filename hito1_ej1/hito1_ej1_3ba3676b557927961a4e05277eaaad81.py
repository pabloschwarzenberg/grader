#Nota final
PT = float(input("Ingrese PT: "))
PI = float(input("Ingrese PI: "))
NE = float(input("Ingrese NE: "))
PP = float(input("Ingrese PP: "))

NF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print(round(NF, 1))