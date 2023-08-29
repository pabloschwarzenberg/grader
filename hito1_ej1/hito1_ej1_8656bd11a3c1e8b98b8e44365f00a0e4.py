#Sacar promedio de acuerdo a la formula señalada

nota1 = float(input("ingrese el Nota de Tareas: "))
nota2 = float(input("ingrese el Nota de Interrogaciones: "))
nota3 = float(input("ingrese el Nota de Exámen: "))
nota4 = float(input("ingrese el Nota de Presentación: "))

#calculamos el promedio con la fórmula y redondeamos con la función "round" a 1 decimal
promedio = round((0.3 * nota1) + (0.3 * nota2) + (0.3 * nota3) + (0.1 * nota4), 1)

print("El promedio de sus notas es " + str(promedio))