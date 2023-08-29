#Nota final
#Entrada

PT = eval(input("Ingrese la nota final de las tareas: "))
PI = eval(input("Ingrese la nota final de las Interrogaciones: "))
NE = eval(input("Ingrese la nota final del examen: "))
PP = eval(input("Ingrese la nota final de la presentación: "))

#Proceso

nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
nota_final_v2 = round(nota_final,1)

#Salida

print("La nota final es: ", nota_final_v2)      