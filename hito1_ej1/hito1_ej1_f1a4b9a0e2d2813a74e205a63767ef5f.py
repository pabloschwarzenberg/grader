#Nota final
def calcular_prom_final(PT, PI,NE,PP):
    promedio= 0.3*PT+0.3*PI+0.3*NE+0.1*PP
    promedio_redondeado= round(promedio, 1)
    print("El promedio final es: ", promedio_redondeado)

PT= float(input("Ingrese la nota de sus tareas: "))
PI= float(input("Ingrese la nota de sus interrogaciones: "))
NE= float(input("Ingrese nota del exame: "))
PP= float(input("Ingrese nota de presentacion: "))

calcular_prom_final(PT, PI, NE, PP)
