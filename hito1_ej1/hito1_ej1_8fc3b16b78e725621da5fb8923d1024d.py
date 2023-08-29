#Nota final
PT = float(input("Ingrese su PT: "))
PI = float(input("Ingrese su PI: "))
NE = float(input("Ingrese su NE: "))
PP = float(input("Ingrese su PP: "))

NF = PT*0.3 + PI*0.3 + NE*0.3 + PP*0.1
NF = round(NF, 1)

print("Su promedio final obtenido es:", NF)