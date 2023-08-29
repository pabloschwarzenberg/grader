PT = float(input('Ingrese la nota de sus tareas: '))
PI = float(input('Ingrese la nota de sus Interrogaciones: '))
NE = float(input('Ingrese la nota de su Examen: '))
PP = float(input('Ingrese la nota de su Presentacion: '))

#Calculamos
nota_final = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

print('Su nota final es: ',round(nota_final,2))