#Nota final
PT=eval(input("nota de sus tareas:"))
PI=eval(input("nota de sus interrogaciones:"))
NE=eval(input("nota de su examen:"))
PP=eval(input("nota de su presentancion:"))
Promedio=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print("El promedio de sus 4 notas es:",round(Promedio,1))