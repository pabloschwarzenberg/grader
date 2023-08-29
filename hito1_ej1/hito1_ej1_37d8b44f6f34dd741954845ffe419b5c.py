#Nota final
notaTareas = float(input("Ingrese la nota de su tarea ->")) 
notaInterro = float(input("Ingrese la nota que obtuvo de su interrogación ->"))
notaExamen = float(input("Ingrese la nota que obtuvo en el examen ->"))
notaPresen = float(input("Ingrese la nota que obtuvo en su presentación ->"))

promFinal = 0.3*notaTareas + 0.3*notaInterro + 0.3*notaExamen + 0.1*notaPresen

redondeo = round(promFinal,1)

print("El promedio entre esas cuatro notas es", redondeo)      