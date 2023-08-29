#Nota final
pt = float(input("Ingrese la nota de las tareas >>>"))
pi = float(input("Ingrese la nota de las interrogaciones >>>"))
ne = float(input("Ingrese la nota del exámen >>>"))
pp = float(input("Ingrese la nota de la presentación >>>"))

#Procesamiento
nota_final = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
nota_final_final = round(nota_final, 1)

#Salida
print ("La nota final de la asignatura es", nota_final_final)     