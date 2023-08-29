#Nota final
N_PT=float(input("Tareas: "))
N_PI=float(input("Interrogaciones: "))
N_NE=float(input("Examen: "))
N_PP=float(input("Presentación: "))
promedio=(0.3*N_PT+0.3*N_PI+0.3*N_NE+0.1*N_PP)
aux=round(promedio,1)
print (aux)