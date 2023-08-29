#Nota final
PT=float(input("Ingrese su nota de las tareas:"))
PI=float(input("Ingrese su nota de las interrogaciones:"))
NE=float(input("Ingrese su nota del examen:"))
PP=float(input("Ingrese su nota de presentación"))
Promedio_F=((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))
Promedio_F1=round(Promedio_F,1)
print("El promedio final es de:",Promedio_F1)    