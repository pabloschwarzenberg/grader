#Nota final
print("Solo ingresar numeros enteros")
PT=float(input("ingrese la notas de la tarea: "))
PI=float(input("ingrese la nota de la interrogacion: "))
NE=float(input("ingrese nota examen: "))
PP=float(input("ingrese nota presentacion: "))
promedio=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print(round(promedio,1))

