#Nota final
PT=input("Escribe tu promedio de tareas:")
PI=input("Escribe tu promedio de interrogación:")
NE=input("Escribe tu nota examen:")
PP=input("Escribe tu nota presentación:")
notafinal=(0.3*float(PT))+(0.3*float(PI))+(0.3*float(NE))+(0.1*float(PP))
print(round(notafinal,1))