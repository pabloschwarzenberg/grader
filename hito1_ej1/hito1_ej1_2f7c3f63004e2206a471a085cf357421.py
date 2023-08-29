#Nota final
PT = float(input("Ingrese la nota de su tarea: "))
PI = float(input("Ingrese la nota de la interrogación: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de la presentación: "))

nota_final = 0.3*(PT)+0.3*(PI)+0.3*(NE)+0.1*(PP)

resultado = "{0:.1f}".format(nota_final)

print(resultado)



   