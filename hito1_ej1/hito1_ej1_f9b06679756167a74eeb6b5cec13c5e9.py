#Nota final
PT= float(input("ingrese el promedio de esta asignatura(TAREAS):"))
PI= float(input("ingrese el promedio de esta asignatura(INTERROGACIONES):"))
NE= float(input("ingrese el promedio de esta asignatura(EXAMEN):"))
PP= float(input("ingrese el promedio de esta asignatura(PRESENTACION):"))
promedio= (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("{0:1f}".format(promedio))