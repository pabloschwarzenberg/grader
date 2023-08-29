#Nota final
PT =float(input("Ingrese su promedio de Tareas"))
PI =float(input("Ingrese su promedio de Interrogaciones"))
NE =float(input("Ingrese su nota del Examen"))
PP =float(input("Ingrese su nota de presentacion"))

PF =(0.3*PT+0.3*PI+0.3*NE+0.1*PP)
print(round(PF,1))