#Nota final
PT = float(input("ingrese su nota de las tareas")) 
PI = float(input("ingrese su nota de las interrogaciones"))   
NE = float(input("ingrese su nota del examen"))   
PP = float(input("ingrese su nota de la presentación"))   
promedio = float((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))

print (round(promedio,1))