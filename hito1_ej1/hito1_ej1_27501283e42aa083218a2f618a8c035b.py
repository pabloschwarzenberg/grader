#Nota final
NE = float(input("total de notas de sus examenes"))
PP = float(input("total de notas de sus presentaciones")) 
PT = float(input("total de notas de sus tareas")) 
PI = float(input("total de notas de sus interrogaciones"))
promedio =  0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(promedio)
redondeo = round(promedio)
print(redondeo)