#Nota final
def promedio(PT,PI,NE,PP):
    return (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
PT=float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE=float(input("Ingrese nota de examen: "))
PP = float(input("Ingrese nota de presentacion: "))

promediofinal=promedio(PT,PI,NE,PP)
print("El promedio final es: ",round(promediofinal,1))