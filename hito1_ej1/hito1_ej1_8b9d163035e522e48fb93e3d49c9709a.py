#Nota final
NUMERO = []
PT= float(input("NOTA TAREAS:"))
PI= float(input("NOTA INTERROGACIONES:"))
NE= float(input("NOTA EXAMEN:"))
PP= float(input("NOTA PRESENTACION:"))

PF=0.3*PT+0.3*PI +0.3*NE+0.1*PP
print(round(PF,1))