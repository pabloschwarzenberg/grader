#Nota final
PT = (float(input("Ingrese nota de Tareas:")))
PI = (float(input("Ingrese nota de Interrogacion:")))
NE = (float(input("Ingrese nota de Examen:")))
PP = (float(input("Ingrese nota de Presentacion:")))

resultado = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
print(round(resultado,1))      