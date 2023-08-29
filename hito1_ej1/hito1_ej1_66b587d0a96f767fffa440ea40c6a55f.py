#Nota final
#Nota Final
#Entradas:
PT = float(input("La calificación por tareas es: "))
PI = float(input("La calificación por interrogaciones es: "))
NE = float(input("La calificación por examen es: "))
PP = float(input("La calificación por presentación es: "))

#Ecuación
pro_fin = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

if pro_fin >= 1.0 and pro_fin <= 7.0:
    resultado = round(pro_fin,1)

    print("Tu promedio final es: " + str(resultado))
else:
    print("Tu promedio está fuera de rango")