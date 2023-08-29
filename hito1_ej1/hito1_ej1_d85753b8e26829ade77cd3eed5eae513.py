PT =float(input("Ingrese su promedio de tareas"))
PI =float(input("Ingrese su promedio de interrogaciones"))
NE =float(input("Ingrese su nota del examen"))
PP =float(input("Ingrese su nota del presentacion"))

PF =(0.3*PT+0.3*PI+0.3*NE+0.1*PP)
print(round(PF,1))