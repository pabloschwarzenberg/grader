#Nota final
print("Vamos a calcular tu promedio final")
PT=float(input("Ingresa el promedio de las tareas: "))
PI=float(input("Ingresa el promedio de las interrogaciones: "))
NE=float(input("Ingresa la nota que obtuviste en el exámen: "))
PP=float(input("Ingresa la nota de la presentación: "))
NF=round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1)
print("Tu nota final es "+str(NF))