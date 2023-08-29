#0.3PT + 0.3PI + 0.3NE + 0.1PP
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
tarea = float(input('Ingrese PT:'))
interrogacion = float(input('Ingrese PI:'))
examen = float(input('Ingrese NE:'))
presentacion = float(input('Ingrese PP:'))

nota = tarea*0.3 + interrogacion*0.3 + examen*0.3 + presentacion*0.1 
nota =round(nota,1)

print('Tu nota final es:',nota)  
     