#Nota final
#Nota final
PT = eval(input("ingrese su nota de las tareas:"))
PI = eval(input("ingrese su nota de las interrogaciones:"))
NE = eval(input("ingrese su nota de los examenes:"))
PP = eval(input("ingrese su nota de las presentaciones:"))
multiplicacion1 = 0.3 * PT
print("la nota final de la tarea es: ", multiplicacion1)
multiplicacion2 = 0.3 * PI
print("la nota final de las interrogaciones es:", multiplicacion2)
multiplicacion3 = 0.3 * NE
print("la nota final de los es examenes es:", multiplicacion3)
multiplicacion4 = 0.1 * PP
print("la nota final de las presentaciones es:", multiplicacion4)
promedio = multiplicacion1 + multiplicacion2 + multiplicacion3 + multiplicacion4
print("despues de un par de calculos su promedio final es:", promedio)