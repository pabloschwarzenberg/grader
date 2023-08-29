#Nota final
PT = float(input())
PI = float(input())
NE = float(input())
PP = float(input())

ponderacion = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
redondeo = round(ponderacion, 1)
print(redondeo)