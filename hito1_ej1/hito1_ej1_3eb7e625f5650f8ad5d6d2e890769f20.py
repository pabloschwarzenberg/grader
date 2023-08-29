#Nota final
pt = float(input("Ingrese la nota de sus tareas: "))
nota_pt = ((pt*3)/10)

pi = float(input("Ingrese la nota de las interrogaciones: "))
nota_pi = ((pi*3)/10)

ne = float(input("Ingrese la nota de su examen: "))
nota_ne = ((ne*3)/10)

pp = float(input("Ingrese la nota de su presentaciÃ³n: "))
nota_pp = ((pp*1)/10)

promedio_final = float(nota_pt + nota_pi + nota_ne + nota_pp)
print("su promedio final es ",round(promedio_final,1))