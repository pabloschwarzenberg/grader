#Nota final
PT = float(input("Ingrese su PT: "))
PI = float(input("Ingrese su PI: "))
NE = float(input("Ingrese su NE: "))
PP = float(input("Ingrese su PP: "))

promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Tu promedio final es:", round(promedio_final, 1))