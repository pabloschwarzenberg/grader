#Nota final
#ENTRADA
PT = float(input("ingrese la nota de Tareas "))
PI = float(input("ingrese la nota de Interrogaciones "))
NE = float(input("ingrese la nota de Examen "))
PP = float(input("ingrese la nota de Presentacions "))

#PROCESO
PF = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
final = float(round(PF, 1))

#SALIDA
print("El promedio final es ", final)