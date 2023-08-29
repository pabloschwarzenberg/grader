#Nota final
PT=float(input("Nota por Tareas: "))
PI=float(input("Nota por interrogantes: "))
NE=float(input("Nota por exámentes: "))
PP=float(input("Presentacíón: "))

x= PT*0.3 + 0.3*PI +0.3*NE + 0.1*PP
x1= round(x, 1)
print(x1)