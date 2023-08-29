#Nota final
PT= float(input("ingrese nota tareas: "))
PI= float(input("ingrese nota interrogaciones: "))
NE= float(input("ingrese nota examen: "))
PP= float(input("ingrese nota presentacion: "))
if 7>PT>1 and 7>PI>1 and 7>NE>1 and 7>PP>1:
    promedio= round((0.3*PT+0.3*PI+0.3*NE+0.1*PP),1)
    print("Promedio final:",promedio)
else:
    print("Valor erroneo")