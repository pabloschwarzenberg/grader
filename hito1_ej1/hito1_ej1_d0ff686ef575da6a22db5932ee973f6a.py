#Nota final
PT=float(input("Ingrese nota de tareas :"))
PI=float(input("Ingrese notas de interrogaciones :"))
NE=float(input("Ingrese nota de examen :"))
PP=float(input("Ingrese nota de presentacion :"))

SUMAPROM = 0.3*PT+0.3*PI+0.3*NE+0.1*PP
SUMAPROM = round(SUMAPROM,1)
print("la suma es"+str(SUMAPROM))

print("Fin del programa")      