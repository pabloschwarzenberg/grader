#Nota final
PT = float(input("Ingrese su promedio de las tareas"))
PI = float(input("Ingrese su promedio de las interrogaciones"))
NE = float(input("Ingrese su nota del examen"))
PP = float(input("Ingrese su promedio de presentación"))

PromFinal = round((PT*0.3 + PI*0.3 + NE* 0.3 + PP*0.1), 1) 
print("Su promedio final es",PromFinal)

