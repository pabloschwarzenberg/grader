#Nota final
PT = float(input("Ingrese su nota de tareas realizadas: "))
PI = float(input("Ingrese su nota de interrogaciones realizadas: "))
NE = float(input("Ingrese su nota de examenes realizadas: "))
PP = float(input("Ingrese su nota de presentaciones realizadas: "))

PF= (0.3*PT)+ (0.3*PI)+(0.3*NE)+(0.1*PP)
print("\nEl promedio final de estas notas es: ",PF)     