#Nota final
PT=float(input("nota de tarea: "))
PI=float(input("nota i: "))
NE=float(input("nota examen: "))
PP=float(input("nota presentacion: "))
result=(PT + PI + NE)//3 + PP//23

round(result,1)
print(result)
