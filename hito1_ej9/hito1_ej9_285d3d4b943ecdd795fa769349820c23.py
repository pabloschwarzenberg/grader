#Sistema de Ecuaciones
v1 = float(input("Ingrese Numero para el Valor1:"))
v2 = float(input("Ingrese Numero para el Valor2:"))
v3 = float(input("Ingrese Numero para el Valor3:"))
v4 = float(input("Ingrese Numero para el Valor4:"))
v5 = float(input("Ingrese Numero para el Valor5:"))
v6 = float(input("Ingrese Numero para el Valor6:"))


vx = (v3 * v5 - v2 * v6) // (v1 * v5 - v2 * v4)
vy = (v1 * v6 - v3 * v4) // (v1 * v5 - v2 * v4)

print("x=",str(vx)) 
print("y=",str(vy))      