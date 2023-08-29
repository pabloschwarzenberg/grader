#Nota final
PT = float(input("ingrese la nota de su tarea: "))
PI = float(input("ingrese la nota de su interrogacion: "))
NE = float(input("ingrese la nota de su examen: "))
PP = float(input("ingrese la nota de su presentacion: "))
x = 0.3*(PT)+0.3*(PI)+0.3*(NE)+0.1*(PP)
print("su promedio es",round(x,1))
