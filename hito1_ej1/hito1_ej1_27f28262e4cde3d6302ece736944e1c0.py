PT=eval(input("nota final de tareas:"))
PI=eval(input("interrogaciones:"))
NE=eval(input("examen:"))
PP=eval(input("presentacion:"))

PF=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
round(PF)
print("el promedio final es:",PF)
