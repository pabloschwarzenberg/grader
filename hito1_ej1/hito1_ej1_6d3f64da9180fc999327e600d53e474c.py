#Nota final
PT = eval(input("Ingrese su nota de tareas:"))
PI = eval(input("Ingrese su nota de interrogaciones:"))
NE = eval(input("Ingrese su nota de examen:"))
PP = eval(input("Ingrese su nota de presentacion:"))
N1 = 0 , 3 * PT
print("La nota de final de tareas es:", N1)
N2 = 0 , 3 * PI
print("La nota final de interrogaciones es:", N2)
N3 = 0 , 3 * NE
print("La nota final de examenes es:", N3)
N4 = 0 , 1 * PP
print("La nota final de presentaciones es:", N4)
Promedio = (N1) + (N2) + (N3) + (N4)
print("El promedio final es:", Promedio)