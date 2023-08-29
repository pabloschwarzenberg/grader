#Nota final
PT = float(input("Por favor ingrese su nota de las tareas: "))
PI = float(input("por favor ingrese su nota de las interrogaciones: "))
NE = float(input("Por favor ingrese su nota de los examenes: "))
PP = float(input("Por favor ingrese su nota de las presentaciones: "))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Su promedio final es de: ", round(NF,1))