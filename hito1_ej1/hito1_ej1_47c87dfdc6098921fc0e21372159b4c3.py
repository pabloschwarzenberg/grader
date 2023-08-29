PT=eval(input("Tareas:"))
PI=eval(input("Interrogaciones:"))
NE=eval(input("Examen:"))
PP=eval(input("Presentacion:"))
PT=(PT/100)*30
PI=(PI/100)*30
NE=(NE/100)*30
PP=(PP/100)*10
PRO=PT+PI+NE+PP
PRO= round(PRO,1)
print("Promedio:",+PRO)