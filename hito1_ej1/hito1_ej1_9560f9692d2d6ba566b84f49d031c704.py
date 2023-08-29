#NOTA FINAL

PT=float(input("ingrese nota de tareas: "))
PI=float(input("ingrese nota de interrogantes: "))
PE=float(input("ingrese nota de examen: "))
PP=float(input("ingrese nota de examen: "))

PF=(0.3*PT+0.3*PI+0.3*PE+0.1*PP)

n=round(PF,1)


print("promedio final= "+str(n))

