#Nota final
pt=float(input("INGRESE NOTA TAREAS: "))
pi=float(input("INGRESE NOTA INTERROGACION: "))
ne=float(input("INGRESE NOTA EXAMEN: "))
pp=float(input("INGRESE NOTA PRESENTACION: "))

fpt= pt*0.3
fpi= pi*0.3
fne= ne*0.3
fpp= pp*0.1
promedio=fpt+fpi+fne+fpp
redon=round(promedio,1)
print(redon)