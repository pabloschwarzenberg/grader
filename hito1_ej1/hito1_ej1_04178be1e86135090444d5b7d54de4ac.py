#Realiza un programa para preguntar al usuario cuatro notas:
#PT = Tareas
#PI = Interrogaciones
#NE= Examen
#PP = Presentacion
#Con ellas calcula el promedio final usando la siguiente fórmula: 0.3PT + 0.3PI + 0.3NE + 0.1PP
#Imprime el resultado redondeado a un decimal. 
PT = float(input("Ingrese su nota de tareas: "))
PI = float(input("Ingrese su nota de interrogaciones: "))
NE = float(input("Ingrese su nota de examen: "))
PP = float(input("Ingrese su nota de presentacion: "))
pro_final = (PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1)
redondeo = round(pro_final, 1)
print("El promedio final es: " + str (redondeo))