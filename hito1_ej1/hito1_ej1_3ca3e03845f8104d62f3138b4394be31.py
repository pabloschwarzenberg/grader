#Nota final
PT = float(input("Ingrese nota de tareas: ")) 
PI = float(input("Ingrese nota de interrogaciones: "))
PE = float(input("Ingrese nota de examen: "))
PP = float(input("Ingrese nota de presentacion: "))

NF = (0.3*PT)+(0.3*PI)+(0.3*PE)+(0.1*PP)

print(round(NF,1))
    