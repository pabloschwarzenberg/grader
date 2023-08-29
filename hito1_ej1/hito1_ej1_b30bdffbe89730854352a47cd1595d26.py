#Nota final
print("Ingrese las notas solicitadas, con una cifra decimal")
tareas=float(input("ingrese nota de tareas(PT): "))
inter=float(input("ingrese nota de interrogaciones(PI): "))
examen=float(input("ingrese nota del examen(NE): "))
pres=float(input("ingrese nota de presentacion(PP): "))
#se calcula la nota ponderada
nota=0.3*tareas+0.3*inter+0.3*examen+0.1*pres
#se amplifica por 10, se pasa a entero para conservar 2 cifras
#y se vuelve a dividir por 10 para dejar un decimal
nota=round(nota,1)


#se imprime un mensaje con la nota final
print("su nota final del ramo es: ",nota)    