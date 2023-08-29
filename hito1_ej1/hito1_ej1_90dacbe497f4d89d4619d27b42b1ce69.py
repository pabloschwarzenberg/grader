#Nota final
#Nota final
#PROMEIOS Y NOTAS
PT = float(input("Ingrese el promedio de tareas: "))
PI = float(input("Ingrese el promedio de interrogaciones: "))
NE = float(input("Ingrese el nota de examen: "))
PP = float(input("Ingrese el promedio de presentaciones: "))
#FÓRMULA PROMEDIO FINAL
NTF = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
#NOTA FINAL
print("La nota final es: ",(round(NTF, 2)))   