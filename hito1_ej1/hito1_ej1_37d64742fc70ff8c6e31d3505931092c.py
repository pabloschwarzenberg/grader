#Nota final
PT = eval(input("Ingrese nota de sus tareas :"))
PI = eval(input("Ingrese nota de sus interrogaciones :"))
NE = eval(input("Ingrese nota de sus examen :"))
PP = eval(input("Ingrese nota de sus presentacion :"))
promedio = PT * 0.3 + PI * 0.3 + NE * 0.3 + PP * 0.1
print("Tu promedio es {0:.1f}".format(promedio))