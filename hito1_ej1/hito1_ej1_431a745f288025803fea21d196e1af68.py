#Nota final
PT = float(input("cual es su nota de tareas: ")) 
PI = float(input("su nota de interrogaciones: "))
PE = float(input("su nota de examen: "))
PP = float(input("su nota de presentacion: "))

promediofinal = (0.3*PT)+(0.3*PI)+(0.3*PE)+(0.1*PP)
print("Su promedio ",promediofinal)
print(round(promediofinal,1))