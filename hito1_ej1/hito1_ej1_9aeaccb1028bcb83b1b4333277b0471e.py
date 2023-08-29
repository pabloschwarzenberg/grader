#Nota final
PT = eval(input("Escriba su nota de tareas: "))

PI = eval(input("Escriba su nota de interrogaciones: "))

NE = eval(input("Escriba su nota de examen: "))

PP = eval(input("Escriba su nota de presentaciones: "))

NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

print("Su promedio final es: ",NF)