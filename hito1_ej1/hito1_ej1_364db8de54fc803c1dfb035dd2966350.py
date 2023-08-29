#Solicitar notas
PT = float(input("ingrese calificacion de sus tareas: "))
PI = float(input("ingrese calificacion de sus interrogaciones:"))
NE = float(input("ingrese calificacion de su examen: "))
PP = float(input("ingrese calificacion de su presentacion: "))
#Calculo
promedio_final = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
promedio_final = round(promedio_final,1)
#Resultado
print ("promedio final es:" , promedio_final)