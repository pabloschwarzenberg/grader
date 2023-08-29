#Nota final
print("while con evento")
promedio, total, contar = 0.0, 0, 0
grado=float(input("Introduzca la nota de un estudiante (-1 para salir): "))
while grado != -1:
    total = total + grado
    print("total",total)
    contar = contar + 1
    print("contar",contar)
grado=float(input("Introduzca la nota de un estudiante (-1 para salir): "))
promedio = total / contar
promedio2 = round(promedio,1)
print ("Promedio de notas del grado escolar es: " + str(promedio2))   