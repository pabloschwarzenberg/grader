#Nota final
PI = float(input("Ingrese un valor: "))
NE = float(input("Ingrese un valor: "))
PP = float(input("Ingrese un valor: "))
PT = float(input("Ingrese un valor: "))

nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("La nota final es: " ,round(nota_final,1))