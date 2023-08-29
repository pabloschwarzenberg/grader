#Nota final
print("ingresar numeros en este formato(6,56 = 6.56)")
print("")
PT = float(input("ingrese la nota de Tareas : "))
PI = float(input("ingrese la nota de Interrogaciones: "))
NE = float(input("ingrese la nota de Examen: "))
PP = float(input("ingrese la nota de Presentacion: "))

prom = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP,1)
print("El promedio final es: ",prom)      