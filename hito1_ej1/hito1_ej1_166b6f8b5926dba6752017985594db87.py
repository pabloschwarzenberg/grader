#Nota final
PT=float(input("Ingrese la nota de sus Tareas:\n"))
PI=float(input("Ingrese la nota de sus Interrogaciones:\n"))
NE=float(input("Ingrese la nota de sus Examenes:\n"))
PP=float(input("Ingrese la nota de su Presentacion:\n"))

notafinal=(0.3)*PT + (0.3)*PI + (0.3)*NE + (0.1)*PP
n=round(notafinal,1)
print(n)