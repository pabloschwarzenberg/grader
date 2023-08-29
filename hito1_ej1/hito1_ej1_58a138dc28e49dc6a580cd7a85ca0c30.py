PI = eval(input("mencione valor interrogantes: "))
NE = eval(input("mencione valor del examen: "))
PP = eval(input("mencione valor de la presentacion: "))
PT = eval(input("mencione el valor de las tareas: "))
if PI > 0 or NE > 0 or PP >0 or PT > 0:
    PROMEDIO_FINAL = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
    PROMEDIO_FINAL = round(PROMEDIO_FINAL , 1)
    print("el promedio final es: " ,PROMEDIO_FINAL,)
else:
    print("no se puede calcular notas negativas")
