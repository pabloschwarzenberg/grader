#Nota final

PT = float(input("ingresa nota de tareas: "))

while PT >= 7.0 or PT <= 1.0:
    print("\nNota inválida")
    PT = float(input("ingresa nota de tareas: "))
    
PI = float(input("ingresa nota de interrogaciones: "))
 
while PI >= 7.0 or PI <= 1.0:
    print("\nNota inválida")
    PI = float(input("ingresa nota de tareas: "))

NE = float(input("ingresa nota del examen: "))
 
while NE >= 7.0 or NE <= 1.0:
    print("\nNota inválida")
    NE = float(input("ingresa nota de tareas: "))

PP = float(input("ingresa nota de presentaciones: "))
 
while PP >= 7.0 or PP <= 1.0:
    print("\nNota inválida")
    PP = float(input("ingresa nota de tareas: "))

promedio_final = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print(round(promedio_final, 1))