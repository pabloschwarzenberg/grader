    #Nota Final
print("Ingrese nota de Tareas")
p_tareas = float(input())
print("Ingrese nota de Interrogaciones")
p_inter = float(input())
print("Ingrese nota de Examen")
n_examen = float(input())
print("Ingrese nota de Presentacion")
p_presentacion = float(input())

p_final = ((0.3*p_tareas)+(0.3*p_inter)+(0.3*n_examen)+(0.1*p_presentacion))

print("la nota final es",round(p_final, 1))  