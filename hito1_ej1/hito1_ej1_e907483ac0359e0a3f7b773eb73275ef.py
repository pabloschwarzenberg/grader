#Nota final
#Nota final

suma= 0
PT= input("ingrese nota de tareas:")
PI= input("ingrese nota de interrogaciones:")
NE= input("ingrese nota de examen:")
PP= input("ingrese nota de presentacion:")

PT= (float(PT) * 0.3)
PI= (float(PI) * 0.3)
NE= (float(NE) * 0.3)
PP= (float(PP) * 0.1)

suma= PT + PI + NE + PP
print("La nota final es:",(suma, 1))