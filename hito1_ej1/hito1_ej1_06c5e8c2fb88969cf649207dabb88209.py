#Nota final
# Solicitar al usuario ingresar las cuatro notas
PT = float(input("Ingresa la nota de PT: "))
PI = float(input("Ingresa la nota de PI: "))
NE = float(input("Ingresa la nota de NE: "))
PP = float(input("Ingresa la nota de PP: "))

# Calcular el promedio final
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Redondear el promedio final a un decimal
promedio_final = round(promedio_final, 1)

# Imprimir el resultado
print("El promedio final es:", promedio_final)      