#Nota final
PT=float(input("Ingrese nota de Tareas ",))
PI=float(input("Ingrese nota de Interrogaciones ",))
NE=float(input("Ingrese nota de Examenes ",))
PP=float(input("Ingrese nota de Presentaciones ",))
promedio=(0.3*PT+0.3*PI+0.3*NE+0.1*PP)
print(round(promedio,1))