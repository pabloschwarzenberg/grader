#Nota final
PT = float(input("notas de las tareas: "))
PI = float(input("notas de las interrogaciones: "))
NE = float(input("notas de los examenes: "))
PP = float(input("notas de las presentaciones: "))

promedio_final =(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print(round(promedio_final,1))       