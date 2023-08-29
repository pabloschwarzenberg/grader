#Nota final
PT= eval (input ("nota tareas:"))
PI= eval (input ("nota interrogaciones:"))
NE= eval (input ("nota examen:"))
PP= eval (input ("nota presentacion:"))

Nf= (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print("nota final:", round (Nf,1))