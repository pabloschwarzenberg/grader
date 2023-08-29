#Nota final
PT = (float(input("nota de tarea: ")))
PI = (float(input("nota de interrogaciones: ")))
NE = (float(input("nota de examen: ")))
PP = (float(input("nota de presentacion: ")))

promedio = 0.3* PT + 0.3* PI + 0.3* NE + 0.1* PP
valor = round(promedio,1)
print("el promedio final es: ",valor)

       