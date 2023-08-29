#Nota final
PT = float(input("Ingrese Nota de la Tarea: "))
PI = float(input("Ingrese Nota de la interrogación: ")) 
NE = float(input("Ingrese Nota del Examen: ")) 
PP = float(input("Ingrese Nota de la Presentación: "))


#notaFinal = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0,1 * PP)
notaFinal = float(0.3 * PT) + float(0.3 * PI) + float(0.3 * NE) + float(0.1 * PP)

#print(type(notaFinal))

#print("El promedio de las notas es:", notaFinal)
print("El promedio de las notas es:", round(notaFinal,1))
