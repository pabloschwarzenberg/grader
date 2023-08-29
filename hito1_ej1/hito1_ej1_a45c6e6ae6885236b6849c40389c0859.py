#Nota final
PT = float(input("Ingrese la nota de tareas "))
PI = float(input("Ingrese la nota de interrogaciones "))
NE = float(input("Ingrese la nota de examenes "))
PP = float(input("Ingrese la nota de presentacion "))

promediofinal = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
con_un_decimal = round(promediofinal, 1)
print(con_un_decimal)      