#Nota final

PT=float(input("Notas Tareas"))
PI=float(input("Notas Interrogaciones"))
NE=float(input("Notas Examen"))
PP=float(input("Notas Presentacion"))

PT_1=0.3*PT
PI_1=0.3*PI
NE_1=0.3*NE
PP_1=0.1*PP

Resultado= (PT_1 + PI_1 + NE_1 + PP_1)

print (round(Resultado,1))