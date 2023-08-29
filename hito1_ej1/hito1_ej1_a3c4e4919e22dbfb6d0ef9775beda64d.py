#ingrese nota de tareas
PT = float(input("introduzca su nota de tareas: "))

while PT >= 7.0 or PT <= 1.0:
    print("\nNota inválida")
    PT = float(input("introduzca su nota de tareas: "))
    
#ingrese nota de interrrogaciones  
PI = float(input("introduzca su nota de interrogaciones: "))
 
while PI >= 7.0 or PI <= 1.0:
    print("\nNota inválida")
    PI = float(input("introduzca su nota de tareas: "))
    
#ingrese nota del examen
NE = float(input("introduzca su nota del examen: "))
 
while NE >= 7.0 or NE <= 1.0:
    print("\nNota inválida")
    NE = float(input("introduzca su nota de tareas: "))

#ingrese nota de presentaciones

PP = float(input("introduzca su nota de presentaciones: "))
 
while PP >= 7.0 or PP <= 1.0:
    print("\nNota inválida")
    PP = float(input("introduzca nota de tareas: "))

promedio_final = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

#imprimir promedio

print(round(promedio_final, 1))