#Nota final



PT= eval(input("Ingrese nota de tareas: "))
PI= eval(input("Ingrese nota de interrrogaciones: "))
NE= eval(input("Ingrese nota de exámen: "))
PP= eval(input("Ingrese nota de presentación: "))

PF= (0.3*PT) + (0.3*PI)+ (0.3*NE) + (0.1*PP)

print(round((0.3*PT) + (0.3*PI)+ (0.3*NE) + (0.1*PP),1))      