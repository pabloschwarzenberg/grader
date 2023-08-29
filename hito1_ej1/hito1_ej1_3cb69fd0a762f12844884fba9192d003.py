#Nota final
Porcentaje_primera_Solemne = float(strInput[8:10])
examen_solemne1 = float(strInput[10:12])
examen_solemne1 = examen_solemne1 / 10

Porcentaje_segunda_solemne = float(strInput[12:14])
examen_solemne2 = float(strInput[14:16])
examen_solemne2 = examen_solemne2 / 10
    
Porcentaje_tarea = float(strInput[16:18])
tarea = float(strInput[18:20])
tarea = tarea / 10

Porcentaje_actividad = float(strInput[20:22])
actividad = float(strInput[22:24])
actividad = actividad / 10

Porcentaje_EDX = float(strInput[24:26])
EDX = float(strInput[26:28])
EDX = EDX / 10

totalFinal = ( examen_solemne1 + examen_solemne2 + tarea + actividad+ EDX ) / 5

print("Fecha: ", Dia, "/", Mes, "/", Año)
print("La Solemne 1 que corresponde al %1.2f" % Porcentaje_primera_Solemne, " porciento la nota es %.1f" % examen_solemne1 )
print("La Solemne 2 que corresponde al %1.2f" % Porcentaje_segunda_solemne, " porciento la nota es %.1f" % examen_solemne2 )
print("La Tarea que corresponde al %1.2f" % Porcentaje_tarea, " porciento la nota es %.1f" % tarea )
print("Las Actividades que corresponde al %1.2f" % Porcentaje_actividad, " porciento la nota es %.1f" % actividad )
print("La Nota de EDX que corresponde al %1.2f" % Porcentaje_EDX, " porciento la nota es %.1f" % EDX )

print("La nota de presentación corresponde a: %.1f" % totalFinal )

print("Felicitaciones esta eximido")
      