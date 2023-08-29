#Nota final
pt=float(input("Nota de Tareas"))
pi=float(input("Nota de Interrogaciones"))
ne=float(input("Nota de examen"))
pp=float(input("Nota de presentacion"))
p1=0.3*pt
p2=0.3*pi
p3=0.3*ne
p4=0.1*pp
nf=round(p1+p2+p3+p4,1)
print("el resultado final es:",nf)