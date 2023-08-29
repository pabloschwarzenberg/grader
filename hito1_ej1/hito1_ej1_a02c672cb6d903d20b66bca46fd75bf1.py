#Nota final
PT = tareas = float(input(" ingrese la nota de sus tareas: "))
PI = interrogaciones = float(input("ingrese la nota de sus interrogaciones:"))
NE = examen = float(input("ingrese la nota de su examen:"))
PP = presentacion = float( input(" ingrese la nota de su presentacion: "))
nota_final = 0.3*PT + 0.3*PI + 0.3*NE+ 0.1*PP
print( "el resultado redondeado a un decimal es: ", round(nota_final,1))      