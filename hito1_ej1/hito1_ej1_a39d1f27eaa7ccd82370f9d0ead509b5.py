#Nota final
PT =float(input("dame tu nota de tarea:"))
PI =float(input("dame tu nota de Interrogaciones"))
NE= float(input("dame tu nota de examen"))
PP = float(input("dame tu nota de  Presentacion :"))
calculo= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
calculo=round(calculo,1)
print(calculo)