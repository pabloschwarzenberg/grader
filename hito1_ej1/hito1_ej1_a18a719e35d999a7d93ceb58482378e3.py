#Nota final
print("Bienvenido a la calculadora de promedios: ")
print()
enter = (input("Presione enter para continuar  "))
print()
PT = float(input("Ingrese la nota que obtuvo en la Tarea: "))
PI = float(input("Ingrese la nota que obtuvo en las Interrogaciones: "))
NE = float(input("Ingrese la nota que obtuvo en el examen: "))
PP = float(input("Ingrese la nota que obtuvo en la presentacion: "))
print()
promedio_final = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print(f"Su promedio final es", promedio_final)
print()     