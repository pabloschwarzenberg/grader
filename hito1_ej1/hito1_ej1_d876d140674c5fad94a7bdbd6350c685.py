#Nota final
PT = float(input('Ingresa la nota de su tarea: ' ))
PI = float(input('Ingresa la nota de Interrogaciones: ' ))
NE = float(input('Ingresa la nota del Examen: ' ))
PP = float(input('Ingresa la nota Presentación: ' ))
notaFinal = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)


print(round(notaFinal,1))