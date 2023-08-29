#Nota final
PT=float(input("Promedio Tareas:"))
PI=float(input("Promedio Interrogaciones:"))
NE=float(input("Nota Exámen:"))
PP=float(input("Promedio Presentación:"))
x=0.3*PT+0.3*PI+0.3*NE+0.1*PP
x=round(x,1)
print(x)      