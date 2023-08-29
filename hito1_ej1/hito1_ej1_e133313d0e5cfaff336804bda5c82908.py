#Nota final
pt=float(input("ingrese la nota de las tareas" ))
pi=float(input("ingrese la nota de las interrogaciones" ))
ne=float(input("ingrese la nota del examen" ))
pp=float(input("ingrese la nota de presentación" ))
nf=round(float(0.3*(pt)+0.3*(pi)+0.3*(ne)+0.1*(pp)),1)
print(nf)