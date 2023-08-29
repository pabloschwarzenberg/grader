#Nota final
PT = float(input("ingresar nota:"))
PI = float(input("ingresar nota:"))
NE = float(input("ingresar nota:"))
PP = float(input("ingresar nota:"))
nota_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
redondeo = round(nota_final, 1)
print(redondeo)  