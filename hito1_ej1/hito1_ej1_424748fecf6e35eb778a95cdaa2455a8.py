#Nota final
PT=input('nota tareas:')
PI=input('nota interrogaciones:')
NE=input('nota examen:')
PP=input('nota presentacion:')
PT=float(PT)
PI=float(PI)
NE=float(NE)
PP=float(PP)
notafinal=((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP))
notafinal=notafinal*10
notafinal=round(notafinal)
notafinal=notafinal/10
print('la nota final es:',notafinal)