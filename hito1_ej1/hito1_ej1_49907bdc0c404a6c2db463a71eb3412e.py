#Nota final
pt=float(input("ingrese nota de tarea"))
pi=float(input("ingrese nota de interrogaciones"))
ne=float(input("ingrese nota de examen"))
pp=float(input("ingrese nota de presentacion"))
nota=0.3*pt
nota2=0.3*pi
nota3=0.3*ne
nota4=0.1*pp
notafinal=round(nota+nota2+nota3+nota4,1)
print("tu nota final es ",notafinal)      